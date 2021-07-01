from django.db import models
from .classificacao import *
from .forma_pagamento import *

class ContaPagar(models.Model):
    SITUACAO = [
        (0, 'A Pagar'),
        (1, 'Pago'),
    ]

    valor = models.FloatField()
    descricao = models.CharField(max_length=60)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(default=None, blank=True, null=True)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    situacao = models.IntegerField(choices=SITUACAO)

    def __str__(self):
        self.option = {
            0: 'A Pagar',
            1: 'Pago',
        }[self.situacao]
        return '{self.descricao} - ${self.valor} ({self.option})'.format(self=self)

    class Meta:
        verbose_name_plural = "Contas a Pagar"
