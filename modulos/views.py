from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Cliente, Marca, Veiculo

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


class MarcaCreate(CreateView):
    model = Marca
    fields = ['nome']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_marcas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Marca"
        context['botao'] = "Cadastrar"
        
        return context


class VeiculoCreate(CreateView):
    model = Veiculo
    fields = ['placa', 'cor', 'marca', 'modelo', 'ano', 'cliente']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_veiculos')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Veículo"
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


class MarcaUpdate(UpdateView):
    model = Marca
    fields = ['nome']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_marcas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Cadastro de Marca"
        context['botao'] = "Atualizar"
        
        return context


class VeiculoUpdate(UpdateView):
    model = Veiculo
    fields = ['placa', 'cor', 'marca', 'modelo', 'ano', 'cliente']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_veiculos')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Cadastro de Veículo"
        context['botao'] = "Atualizar"
        
        return context



#Deletes
class ClienteDelete(DeleteView):
    model = Cliente
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_clientes')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Exclusão de Cliente"
        context['botao'] = "Excluir"
        
        return context


class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_marcas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Exclusão de Marca"
        context['botao'] = "Excluir"
        
        return context


class VeiculoDelete(DeleteView):
    model = Veiculo
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_veiculos')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Exclusão de Veículo"
        context['botao'] = "Excluir"
        
        return context



#Liste
class ClienteList(ListView):
    model = Cliente
    template_name = 'modulos/listas/cliente.html'


class MarcaList(ListView):
    model = Marca
    template_name = 'modulos/listas/marca.html'


class VeiculoList(ListView):
    model = Veiculo
    template_name = 'modulos/listas/veiculo.html'