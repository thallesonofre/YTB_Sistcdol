from django.contrib import admin
from django.urls import path, include
from paginas.views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('modulos.urls')),
    
    #pagina inicial
    path('', Index.as_view(), name="index"),
]
