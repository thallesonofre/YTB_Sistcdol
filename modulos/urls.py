from django.urls import path
from .views import ClienteCreate, MarcaCreate, VeiculoCreate, OleoCreate, FiltroCreate, TrocaCreate
from .views import ClienteUpdate, MarcaUpdate, VeiculoUpdate, OleoUpdate, FiltroUpdate, TrocaUpdate
from .views import ClienteDelete, MarcaDelete, VeiculoDelete, OleoDelete, FiltroDelete, TrocaDelete
from .views import ClienteList, MarcaList, VeiculoList, OleoList, FiltroList, TrocaList



urlpatterns = [
    #create
    path('cadastrar/cliente', ClienteCreate.as_view(), name="cadastrar_cliente"),
    path('cadastrar/marca', MarcaCreate.as_view(), name="cadastrar_marca"),
    path('cadastrar/veiculo', VeiculoCreate.as_view(), name="cadastrar_veiculo"),
    path('cadastrar/oleo', OleoCreate.as_view(), name="cadastrar_oleo"),
    path('cadastrar/filtro', FiltroCreate.as_view(), name="cadastrar_filtro"),
    path('cadastrar/troca', TrocaCreate.as_view(), name="cadastrar_troca"),
    
    
    #Update
    path('editar/cliente/<int:pk>', ClienteUpdate.as_view(), name="editar_cliente"),
    path('editar/marca/<int:pk>', MarcaUpdate.as_view(), name="editar_marca"),
    path('editar/veiculo/<int:pk>', VeiculoUpdate.as_view(), name="editar_veiculo"),
    path('editar/oleo/<int:pk>', OleoUpdate.as_view(), name="editar_oleo"),
    path('editar/filtro/<int:pk>', FiltroUpdate.as_view(), name="editar_filtro"),
    path('editar/troca/<int:pk>', TrocaUpdate.as_view(), name="editar_troca"),
    
    
    #Delete
    path('excluir/cliente/<int:pk>', ClienteDelete.as_view(), name="excluir_cliente"),
    path('excluir/marca/<int:pk>', MarcaDelete.as_view(), name="excluir_marca"),
    path('excluir/veiculo/<int:pk>', VeiculoDelete.as_view(), name="excluir_veiculo"),
    path('excluir/oleo/<int:pk>', OleoDelete.as_view(), name="excluir_oleo"),
    path('excluir/filtro/<int:pk>', FiltroDelete.as_view(), name="excluir_filtro"),
    path('excluir/troca/<int:pk>', TrocaDelete.as_view(), name="excluir_troca"),
    
    
    #Liste
    path('listar/clientes', ClienteList.as_view(), name="listar_clientes"),
    path('listar/marcas', MarcaList.as_view(), name="listar_marcas"),
    path('listar/veiculo', VeiculoList.as_view(), name="listar_veiculos"),
    path('listar/oleo', OleoList.as_view(), name="listar_oleo"),
    path('listar/filtros', FiltroList.as_view(), name="listar_filtros"),
    path('listar/troca',TrocaList.as_view(), name="listar_trocas"),
    
    
]
