from django.shortcuts import render, redirect

from tecno.models import Categoria

def criar_categoria(request):
    nome = request.POST.get('nome')
    
    print(nome)
    
    if request.method == 'POST':
        categoria = Categoria.objects.create(nome = nome)
        return redirect('lista_produto')
    
    categoria = Categoria.objects.all()
    context = {
        'criar_categoria': categoria
    }
   
    return render(request, 'categoria/criar_categoria.html', context = context)