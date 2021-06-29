from django.db import models
from .classificacao import *
from .forma_pagamento import *

class ContaReceber(models.Model):
    SITUACAO = [
        (0, 'A Receber'),
        (1, 'Recebido'),
    ]

    valor = models.FloatField()
    descricao = models.CharField(max_length=60)
    data_expectativa = models.DateField()
    data_recebimento = models.DateField(default=None, blank=True, null=True)
    forma_pagamento = models.OneToOneField(FormaPagamento, on_delete=models.CASCADE)
    classificacao = models.OneToOneField(Classificacao, on_delete=models.CASCADE)
    situacao = models.IntegerField(choices=SITUACAO)

    def __str__(self):
        self.option = {
            0: 'A Receber',
            1: 'Recebido',
        }[self.situacao]
        return '{self.descricao} - ${self.valor} ({self.option})'.format(self=self)

    class Meta:
        verbose_name_plural = "Contas a Receber"
