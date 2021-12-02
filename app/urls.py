from django.urls import path, include

from app.views.index import IndexView, RegisterView, LoginView, PortalCustomerView, LogoutView

urlpatterns = []

urlpatterns += [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('registro', RegisterView.as_view(), name='register'),
    path('portal', PortalCustomerView.as_view(), name='portal'),
    path('logout', LogoutView.as_view(), name='logout')
]
