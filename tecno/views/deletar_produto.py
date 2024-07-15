from django.shortcuts import redirect
from django.contrib import messages

from tecno.models import Produto

def deletar_produto(request, index):
    Produto.objects.filter(index = index).delete()

    messages.success(request, 'Item Deletado!')

    return redirect('lista_produto')