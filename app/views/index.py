from django.contrib import messages
from django.urls import reverse
from django.views.generic import FormView, CreateView

from app.forms import MensagemForm


class IndexView(CreateView):
    form_class = MensagemForm
    template_name = 'index.html'

    def get_success_url(self):
        return reverse('index')

    def form_valid(self, form):
        messages.success(self.request, 'Mensagem enviada com sucesso')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Houve algum erro. Tente novamente.')
        return super(IndexView, self).form_invalid(form=form)
