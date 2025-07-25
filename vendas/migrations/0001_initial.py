# Generated by Django 5.1.1 on 2025-07-18 20:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.fornecedor')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.produto')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=100)),
                ('complemento', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendaFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.fornecedor')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.venda')),
            ],
        ),
        migrations.CreateModel(
            name='VendaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.venda')),
            ],
        ),
    ]
