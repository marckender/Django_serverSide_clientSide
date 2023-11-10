from django.db import models

class Mensagem(models.Model):
    usuario = models.CharField(max_length=255)
    mensagem = models.TextField()
    datahora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} - {self.datahora}'