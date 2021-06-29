from django.db import models
from .classificacao import *
from .forma_pagamento import *
from .situacao_pagar import *

class ContaPagar(models.Model):
    valor = models.FloatField()
    descricao = models.CharField(max_length=60)
    data_pagamento = models.DateField()
    data_vencimento = models.DateField()
    forma_pagamento = models.OneToOneField(FormaPagamento, on_delete=models.CASCADE)
    classificacao = models.OneToOneField(Classificacao, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=20, choices=SituacaoPagar.choices())
