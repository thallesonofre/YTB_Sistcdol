from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Cliente, Marca, Veiculo, Oleo, Filtro, Troca

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


class OleoCreate(CreateView):
    model = Oleo
    fields = ['tipo', 'descricao']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_oleo')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Óleo"
        context['botao'] = "Cadastrar"
        
        return context


class FiltroCreate(CreateView):
    model = Filtro
    fields = ['tipo', 'descricao']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_filtros')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Cadastro de Filtro"
        context['botao'] = "Cadastrar"
        
        return context


class TrocaCreate(CreateView):
    model = Troca
    fields = ['data', 'placa', 'oleo', 'filtro', 'kmpt']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_trocas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Lançar Troca de Óleo"
        context['botao'] = "Lançar"
        
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


class OleoUpdate(UpdateView):
    model = Oleo
    fields = ['tipo', 'descricao']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_oleo')
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Cadastro de Óleo"
        context['botao'] = "Atualizar"
        
        return context


class FiltroUpdate(UpdateView):
    model = Filtro
    fields = ['tipo', 'descricao']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_filtros')
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Cadastro de Filtros"
        context['botao'] = "Atualizar"
        
        return context


class TrocaUpdate(UpdateView):
    model = Troca
    fields = ['data', 'placa', 'oleo', 'filtro', 'kmpt']
    template_name = 'modulos/form.html'
    success_url = reverse_lazy('listar_trocas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Atualizar Troca de ÓLeo"
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


class OleoDelete(DeleteView):
    model = Oleo
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_oleo')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Exclusão de Óleo"
        context['botao'] = "Excluir"
        
        return context


class FiltroDelete(DeleteView):
    model = Filtro
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_filtros')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Exclusão de Filtros"
        context['botao'] = "Excluir"
        
        return context


class TrocaDelete(DeleteView):
    model = Troca
    template_name = 'modulos/form_excluir.html'
    success_url = reverse_lazy('listar_trocas')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['titulo'] = "Excluir Troca de Óleo"
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


class OleoList(ListView):
    model = Oleo
    template_name = 'modulos/listas/oleo.html'


class FiltroList(ListView):
    model = Filtro
    template_name = 'modulos/listas/filtro.html'


class TrocaList(ListView):
    model = Troca
    template_name = 'modulos/listas/troca.html'