from django.urls import path, include
from .views.lista_produto import lista_produto
from .views.criar_produto import criar_produto
from .views.atualizar_produto import atualizar_produto
from .views.deletar_produto import deletar_produto
from .views.criar_ctegoria import criar_categoria
from .views.produto_da_categoria import produto_da_categoria
from .views.lista_categoria import lista_categoria
from .views.lista_categoria import deletar_categoria

urlpatterns = [
    path('', lista_produto, name='lista_produto'),
    path('criar/produto/', criar_produto, name='criar_produto'),
    path('atualizar/produto/<int:index>/', atualizar_produto, name='atualizar_produto'),
    path('deletar/produto/<int:index>/', deletar_produto, name= 'deletar_produto'),
    path('criar/categoria/', criar_categoria, name= 'criar_categoria'),
    path('categoria/produto/<int:index>/', produto_da_categoria, name= 'produto_da_categoria'),
    path('lista/categoria/', lista_categoria, name="lista_categoria"),
    path('deletar/categoria/<int:index>/', deletar_categoria, name= 'deletar_categoria'),
]