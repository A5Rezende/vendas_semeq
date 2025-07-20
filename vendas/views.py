from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CadastroForm
from .models import Perfil, Produto, Venda, VendaFornecedor, VendaProduto, Fornecedor, ProdutoFornecedor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']

        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('lista_vendas')
        else:
            messages.error(request, 'Email ou senha inválidos.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_view(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            # Cria o perfil com nome e CPF
            Perfil.objects.create(
                user=user,
                nome=form.cleaned_data['nome'],
                cpf=form.cleaned_data['cpf']
            )
            return redirect('login')
    else:
        form = CadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def home_view(request):
    return redirect('login')

from django.http import JsonResponse
import json
from .models import Venda, VendaProduto

@login_required
def comprar_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            data_venda = data.get('data_venda')
            valor_total = data.get('valor_total')
            numero = data.get('numero')
            rua = data.get('rua')
            bairro = data.get('bairro')
            cidade = data.get('cidade')
            estado = data.get('estado')
            complemento = data.get('complemento')
            produtos_ids = data.get('produtos_ids', [])

            if not produtos_ids:
                return JsonResponse({'error': 'Nenhum produto recebido'}, status=400)

            venda = Venda.objects.create(
                data=data_venda,
                valor_total=valor_total,
                numero=numero,
                rua=rua,
                bairro=bairro,
                cidade=cidade,
                estado=estado,
                complemento=complemento,
                cliente_id=request.user.id
            )

            id_fornecedores = []

            for produto_id in produtos_ids:
                VendaProduto.objects.create(venda=venda, produto_id=produto_id)

                produto = Produto.objects.get(id=produto_id)
                fornecedores = ProdutoFornecedor.objects.filter(produto=produto)

                id_fornecedores += fornecedores.values_list('fornecedor_id', flat=True) 

            id_fornecedores = list(set(id_fornecedores))
            
            for fornecedor_id in id_fornecedores:
                VendaFornecedor.objects.create(venda=venda, fornecedor_id=fornecedor_id)

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    # GET request
    produtos = Produto.objects.all()
    return render(request, 'comprar.html', {'produtos': produtos})


def encontrar_dados_produto(request, produto_id):
    relations = ProdutoFornecedor.objects.select_related('produto', 'fornecedor').filter(produto_id=produto_id)

    if not relations.exists():
        return JsonResponse({'erro': 'Produto não encontrado'}, status=404)

    # Pegue o produto apenas uma vez (o primeiro já serve)
    produto = relations[0].produto

    fornecedores = []
    for rel in relations:
        fornecedores.append({
            'id': rel.fornecedor.id,
            'nome': rel.fornecedor.nome,
            'cnpj': rel.fornecedor.cnpj
        })

    dados = {
        'id': produto.id,
        'nome': produto.nome,
        'preco_unitario': float(produto.preco_unitario),
        'fornecedores': fornecedores
    }

    return JsonResponse(dados)

from django.db.models import Q

@login_required
def inicio_view(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        vendas = Venda.objects.filter(
            cliente_id=request.user.id,
            vendaproduto__produto__nome__icontains=pesquisa
        ).distinct()
    else:
        vendas = Venda.objects.filter(cliente_id=request.user.id)

    return render(request, 'inicio.html', {'vendas': vendas})

@login_required
def consultar_view(request):
    pesquisa = request.GET.get('pesquisa')

    if pesquisa:
        produtos = Produto.objects.filter(
            produtofornecedor__produto__nome__icontains=pesquisa
        ).distinct()
    else:
        produtos = Produto.objects.all()

    return render(request, 'consultar.html', {'produtos': produtos})