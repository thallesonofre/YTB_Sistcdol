from django.urls import path
from .views import ClienteCreate
from .views import ClienteUpdate
from .views import ClienteDelete
from .views import ClienteList


urlpatterns = [
    #create
    path('cadastrar/cliente', ClienteCreate.as_view(), name="cadastrar_cliente"),
    
    #Update
    path('editar/cliente/<int:pk>', ClienteUpdate.as_view(), name="editar_cliente"),
    
    #Delete
    path('excluir/cliente/<int:pk>', ClienteDelete.as_view(), name="excluir_cliente"),
    
    #Liste
    path('listar/clientes', ClienteList.as_view(), name="listar_clientes"),
]
