from django.shortcuts import render

from tecno.models import Produto

def produto_da_categoria(request, index):

    produto = Produto.objects.filter(categoria = index).all()

    context = {
        'produto_da_categoria': produto
    }
    return render(request, 'categoria/produto_da_categoria.html', context= context)
