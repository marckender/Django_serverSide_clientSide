from django.urls import path
from .views import MensagemListCreateView

urlpatterns = [
    path('mensagens/', MensagemListCreateView.as_view(), name='mensagem-list-create'),
]