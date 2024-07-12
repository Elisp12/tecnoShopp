from django.shortcuts import render, redirect

from tecno.models import Categoria, Produto

def atualizar_produto(request, index):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    categoria = request.POST.get('categoria')
    quantidade = request.POST.get('quantidade')

    produto = Produto.objects.filter(index = index) 

    if request.method == 'POST':
        Produto.objects.filter(index = index).update(nome = nome, descricao = descricao, categoria = Categoria.objects.get(index = categoria), quantidade = quantidade)
        return redirect('lista_produto')
    
    lista_categoria = Categoria.objects.all()

    context = {
        'produto' : produto,
        'categoria': lista_categoria
    }
    return render(request, 'produto/atualizar_produto.html', context = context )
