from django.shortcuts import render, redirect
from django.contrib import messages

from tecno.models import Categoria


def lista_categoria(request):
    l_categoria = Categoria.objects.all()

    context = {
        'lista_categoria': l_categoria
    }

    return render(request, 'categoria/lista_categoria.html', context= context)

def deletar_categoria(request, index):
    del_categoria = Categoria.objects.filter(index = index).delete()

    messages.success(request, 'categoria deletada!')

    return redirect('lista_categoria')