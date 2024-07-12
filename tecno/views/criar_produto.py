from django.shortcuts import render, redirect

from tecno.models import Categoria, Produto


def criar_produto(request):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    categoria = request.POST.get('categoria')
    quantidade = request.POST.get('quantidade')
    
    if request.method == 'POST':
        Produto.objects.create(nome = nome, descricao = descricao, categoria = Categoria.objects.get(index = categoria), quantidade = quantidade)
        return redirect('lista_produto')

    lista_categoria = Categoria.objects.all()

    context = {
        'criar_produto': lista_categoria
    }

    return render(request, 'produto/criar_produto.html', context = context)