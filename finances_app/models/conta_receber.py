from django.db import models
from .classificacao import *
from .forma_pagamento import *
from .situacao_receber import *

class ContaReceber(models.Model):
    valor = models.FloatField()
    descricao = models.CharField(max_length=60)
    data_expectativa = models.DateField()
    data_recebimento = models.DateField()
    forma_pagamento = models.OneToOneField(FormaPagamento, on_delete=models.CASCADE)
    classificacao = models.OneToOneField(Classificacao, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=20, choices=SituacaoReceber.choices())

    class Meta:
        verbose_name_plural = "Contas a Receber"
