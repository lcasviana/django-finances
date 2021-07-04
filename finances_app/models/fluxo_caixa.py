from django.db import models


class FluxoCaixa(models.Model):
    ano = models.IntegerField()
    mes = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        self.mes_str = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro',
        }[self.mes]
        return '{self.ano} {self.mes_str}: ${self.valor}'.format(self=self)

    class Meta:
        verbose_name_plural = 'Fluxo Caixa'
