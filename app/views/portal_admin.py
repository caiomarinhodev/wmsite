from django.contrib import messages
from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django_datatables_view.base_datatable_view import BaseDatatableView

from app.forms import SolicitacaoForm
from app.models import Solicitacao
from app.views.snippet_template import render_block_to_string


class NoPermissionMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class PortalAdminView(LoginRequiredMixin, NoPermissionMixin, ListView):
    login_url = '/login'
    template_name = 'portal_admin/solicitacoes.html'
    model = Solicitacao
    ordering = '-data_cadastro'
    context_object_name = 'solicitacoes'
    paginate_by = 1


class SolicitacoesAdminListJson(BaseDatatableView):
    model = Solicitacao
    columns = ("id", "cliente", "data_cadastro", "produto", "status",)
    order_columns = ("id", "cliente", "data_cadastro", "produto", "status",)
    max_display_length = 500

    def filter_queryset(self, qs):
        return super(SolicitacoesAdminListJson, self).filter_queryset(qs)


class CreateAdminSolicitacao(LoginRequiredMixin, NoPermissionMixin, CreateView):
    login_url = '/login'
    model = Solicitacao
    form_class = SolicitacaoForm
    template_name = 'portal_admin/create_solicitacao.html'
    context_object_name = 'solicitacao'

    def get_success_url(self):
        return reverse_lazy('portal_admin')

    def form_valid(self, form):
        messages.success(self.request, 'Solicitacao criada com sucesso')
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(CreateAdminSolicitacao, self).form_invalid(form)


class UpdateSolicitacao(LoginRequiredMixin, NoPermissionMixin, UpdateView):
    login_url = '/login'
    model = Solicitacao
    template_name = 'portal_admin/edit_solicitacao.html'
    context_object_name = 'solicitacao'
    form_class = SolicitacaoForm

    def get_initial(self):
        data = super(UpdateSolicitacao, self).get_initial()
        return data

    def get_success_url(self):
        return reverse_lazy('portal_admin')

    def get_context_data(self, **kwargs):
        data = super(UpdateSolicitacao, self).get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        messages.success(self.request, 'Solicitacao atualizada com sucesso')
        return super(UpdateSolicitacao, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Houve algum erro, tente novamente')
        return super(UpdateSolicitacao, self).form_invalid(form)


class DeleteSolicitacao(LoginRequiredMixin, NoPermissionMixin, DeleteView):
    """
    Delete a Address
    """
    login_url = '/login'
    model = Solicitacao
    template_name = 'portal_admin/delete_solicitacao.html'
    context_object_name = 'solicitacao'

    def get_context_data(self, **kwargs):
        context = super(DeleteSolicitacao, self).get_context_data(**kwargs)
        collector = NestedObjects(using='default')
        collector.collect([self.get_object()])
        context['deleted_objects'] = collector.nested()
        return context

    def __init__(self):
        super(DeleteSolicitacao, self).__init__()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Solicitacao removida com sucesso')
        return super(DeleteSolicitacao, self).delete(self.request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('portal_admin')


@require_http_methods(["GET"])
def notificar_novo_solicitacao(request):
    solicitacao = Solicitacao.objects.filter(status='Aguardando').last()
    return_str = ''
    if solicitacao:
        context = {'solicitacao': solicitacao, 'user': request.user}
        return_str = render_block_to_string('portal_admin/notificacao.html', context)
    return HttpResponse(return_str)
