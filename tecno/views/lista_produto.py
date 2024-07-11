from django.shortcuts import render

from tecno.models import Produto

def lista_produto(request):
    lista_produto = Produto.objects.all()

    context = {
        'lista_produto': lista_produto
    }
    
    return render(request, 'produto/lista_produto.html', context = context)