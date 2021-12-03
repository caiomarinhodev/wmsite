from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from app.forms import SolicitacaoForm, UserForm
from app.models import Solicitacao


class PortalCustomerView(LoginRequiredMixin, ListView):
    login_url = '/login'
    template_name = 'portal_customer/solicitacoes.html'
    model = Solicitacao
    ordering = '-data_cadastro'
    context_object_name = 'solicitacoes'
    paginate_by = 1


class SolicitacoesListJson(BaseDatatableView):
    model = Solicitacao
    columns = ("id", "data_cadastro", "produto", "status",)
    order_columns = ("id", "data_cadastro", "produto", "status",)
    max_display_length = 500

    def filter_queryset(self, qs):
        print(self.request.user)
        qs = qs.filter(cliente__usuario=self.request.user)
        return super(SolicitacoesListJson, self).filter_queryset(qs)


class CreateSolicitacao(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Solicitacao
    form_class = SolicitacaoForm
    template_name = 'portal_customer/create_solicitacao.html'
    context_object_name = 'solicitacao'

    def get_success_url(self):
        return reverse_lazy('portal')

    def form_valid(self, form):
        messages.success(self.request, 'Solicitacao criada com sucesso')
        self.object = form.save()
        solicitacao = self.object
        solicitacao.cliente = self.request.user.cliente_set.first()
        solicitacao.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(CreateSolicitacao, self).form_invalid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = User
    template_name = 'portal_customer/my_data.html'
    context_object_name = 'user'
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        data = super(ProfileUpdateView, self).get_context_data()
        cliente = self.request.user.cliente_set.last()
        data['city'] = cliente.cidade
        data['district'] = cliente.bairro
        data['address'] = cliente.endereco
        data['number'] = cliente.numero
        data['cep'] = cliente.cep
        data['nome_empresa'] = cliente.nome_empresa
        return data

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        data = form.data
        user = self.get_object()
        cliente = user.cliente_set.last()
        cliente.nome_empresa = data['nome_empresa']
        cliente.endereco = data['address']
        cliente.numero = data['number']
        cliente.bairro = data['district']
        cliente.cidade = data['city']
        cliente.cep = data['cep']
        cliente.save()
        messages.success(self.request, 'Dados atualizados com sucesso')
        return super(ProfileUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(ProfileUpdateView, self).form_invalid(form)
