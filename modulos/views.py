from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Cliente

# Create your views here.

#Creates
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_clientes')
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Cliente"
        context['botao'] = "Cadastrar"
        
        return context


    
#Updates
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'cpf', 'telefone', 'email', 'endereco']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_clientes')
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Cadastro do Cliente"
        context['botao'] = "Atualizar"
        
        return context



#Deletes
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_clientes')



#Liste
class ClienteList(ListView):
    model = Cliente
    template_name = 'modulos/listas/cliente.html'