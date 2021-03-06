from django.urls import path

from app.views.index import IndexView, RegisterView, LoginView, LogoutView, PolicyView
from app.views.portal_admin import PortalAdminView, SolicitacoesAdminListJson, CreateAdminSolicitacao, \
    UpdateSolicitacao, DeleteSolicitacao, notificar_novo_solicitacao
from app.views.portal_customer import SolicitacoesListJson, PortalCustomerView, CreateSolicitacao, ProfileUpdateView

urlpatterns = []

urlpatterns += [
    path('', IndexView.as_view(), name='index'),
    path('policy', PolicyView.as_view(), name='policy'),
    path('login', LoginView.as_view(), name='login'),
    path('registro', RegisterView.as_view(), name='register'),
    path('portal', PortalCustomerView.as_view(), name='portal'),
    path('solicitacao/create/', CreateSolicitacao.as_view(), name='create_solicitacao'),
    path('profile', ProfileUpdateView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('solicitacao/list/json/', SolicitacoesListJson.as_view(), name='solicitacoes_list_json'),

    path('portal/admin/', PortalAdminView.as_view(), name='portal_admin'),
    path('solicitacao/admin/list/json/', SolicitacoesAdminListJson.as_view(), name='solicitacoes_admin_list_json'),
    path('portal/admin/create/', CreateAdminSolicitacao.as_view(), name='create_solicitacao_admin'),
    path('portal/admin/<int:pk>/', UpdateSolicitacao.as_view(), name='update_solicitacao_admin'),
    path('portal/admin/<int:pk>/delete/', DeleteSolicitacao.as_view(), name='delete_solicitacao_admin'),
    path('notify', notificar_novo_solicitacao, name='notify_solicitacao')
]
