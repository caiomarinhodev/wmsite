from django.urls import path, include

from app.views.index import IndexView

urlpatterns = []

urlpatterns += [
    path('', IndexView.as_view(), name='index')
]
