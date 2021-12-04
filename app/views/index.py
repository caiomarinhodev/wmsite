from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, FormView, RedirectView, TemplateView

from app.forms import MensagemForm, UserForm, LoginForm
from app.models import Cliente


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


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return super(LoginView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('portal_admin')
        return reverse('portal')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        data = form.data
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form=form)

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Houve algum erro. Tente novamente.')
        return super(LoginView, self).form_invalid(form=form)


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'register.html'

    def get_success_url(self):
        return reverse('login')

    def form_valid(self, form):
        data = form.data
        user = User.objects.create_user(username=data['username'],
                                        email=data['email'],
                                        password=data['password'])
        cliente = Cliente()
        cliente.usuario = user
        cliente.nome_empresa = data['nome_empresa']
        cliente.save()
        messages.success(self.request, 'Usuario criado com sucesso. Realize Login na Plataforma !')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print(form.errors)
        messages.error(self.request, 'Houve algum erro. Tente novamente.')
        return super(RegisterView, self).form_invalid(form=form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class PolicyView(TemplateView):
    template_name = 'policy.html'
