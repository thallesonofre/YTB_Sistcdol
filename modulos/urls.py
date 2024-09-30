from django.urls import path
from .views import ClienteCreate, MarcaCreate, VeiculoCreate
from .views import ClienteUpdate, MarcaUpdate, VeiculoUpdate
from .views import ClienteDelete, MarcaDelete, VeiculoDelete
from .views import ClienteList, MarcaList, VeiculoList



urlpatterns = [
    #create
    path('cadastrar/cliente', ClienteCreate.as_view(), name="cadastrar_cliente"),
    path('cadastrar/marca', MarcaCreate.as_view(), name="cadastrar_marca"),
    path('cadastrar/veiculo', VeiculoCreate.as_view(), name="cadastrar_veiculo"),
    
    
    #Update
    path('editar/cliente/<int:pk>', ClienteUpdate.as_view(), name="editar_cliente"),
    path('editar/marca/<int:pk>', MarcaUpdate.as_view(), name="editar_marca"),
    path('editar/veiculo/<int:pk>', VeiculoUpdate.as_view(), name="editar_veiculo"),
    
    
    #Delete
    path('excluir/cliente/<int:pk>', ClienteDelete.as_view(), name="excluir_cliente"),
    path('excluir/marca/<int:pk>', MarcaDelete.as_view(), name="excluir_marca"),
    path('excluir/veiculo/<int:pk>', VeiculoDelete.as_view(), name="excluir_veiculo"),
    
    
    #Liste
    path('listar/clientes', ClienteList.as_view(), name="listar_clientes"),
    path('listar/marcas', MarcaList.as_view(), name="listar_marcas"),
    path('listar/veiculo', VeiculoList.as_view(), name="listar_veiculos"),
    
    
]
