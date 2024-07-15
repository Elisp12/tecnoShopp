from django.shortcuts import redirect
from django.contrib import messages

from tecno.models import Categoria


def deletar_categoria(request, index):
    try:

        Categoria.objects.filter(index = index).delete()
        messages.success(request, 'Categoria deletada!')

    except:

        messages.error(request, 'A Categoria não pode ser removida pois tem produtos atrelado a ela!')
        return redirect('lista_categoria')

    return redirect('lista_categoria')