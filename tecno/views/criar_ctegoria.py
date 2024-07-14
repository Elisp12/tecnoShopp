from django.shortcuts import render, redirect

from tecno.models import Categoria

def criar_categoria(request):
    nome = request.POST.get('nome')
    
    print(nome)

    
    if request.method == 'POST':
        categoria = Categoria.objects.update_or_create(nome = nome)

        return redirect('lista_categoria')
    
    categoria = Categoria.objects.all()
    context = {
        'criar_categoria': categoria
    }
   
    return render(request, 'categoria/criar_categoria.html', context = context)