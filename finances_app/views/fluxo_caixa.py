from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from ..models import *

def fluxo_caixa_index(request):
    meses = {
        "Julho": 7,
        "Agosto": 8,
        "Setembro": 9,
        "Outubro": 10,
        "Novembro": 11,
        "Dezembro": 12,
    }
    data = {"meses": meses}
    return render(request, "fluxo_caixa.html", data)

def fluxo_caixa_index_mes(request, mes):
    mes_atual = int(mes)
    mes_anterior = mes_atual - 1
    meses = {
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }
    contas_pagar = ContaPagar.objects.filter(data_vencimento__month=int(mes_atual)).order_by(
        "data_vencimento"
    )
    contas_receber = ContaReceber.objects.filter(
        data_recebimento__month=int(mes_atual)
    ).order_by("data_recebimento")
    receitas_mes_anterior = ContaReceber.objects.filter(data_recebimento__month=mes_anterior).values('data_recebimento__month').annotate(soma_valor=Sum('valor')).order_by()
    despesas_mes_anterior = ContaPagar.objects.filter(data_vencimento__month=mes_anterior).values('data_vencimento__month').annotate(soma_valor=Sum('valor')).order_by()
    data = {
        "receitas_anterior": receitas_mes_anterior,
        "despesas_anterior" : despesas_mes_anterior,
        "mes": meses[mes_atual],
        "receitas": contas_receber,
        "despesas": contas_pagar,
    }
    return render(request, "fluxo_caixa_mes.html", data)
