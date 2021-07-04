from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from ..models import *


def fluxo_caixa_index(request):
    fluxo_caixa_processar()

    meses = {
        'Julho': 7,
        'Agosto': 8,
        'Setembro': 9,
        'Outubro': 10,
        'Novembro': 11,
        'Dezembro': 12,
    }
    data = {
        'meses': meses,
    }
    return render(request, 'fluxo_caixa.html', data)


def fluxo_caixa_index_referencia(request, ano, mes):
    fluxo_caixa_processar()

    mes_atual = mes
    mes_anterior = mes - 1
    meses = {
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro',
    }

    contas_pagar = ContaPagar.objects.filter(
        data_vencimento__year=ano,
        data_vencimento__month=mes_atual)
    contas_receber = ContaReceber.objects.filter(
        data_expectativa__year=ano,
        data_expectativa__month=mes_atual)

    total_pagar = sum(c.valor for c in contas_pagar)
    total_receber = sum(c.valor for c in contas_receber)

    saldo_mes_anterior = FluxoCaixa.objects.get(
        ano=ano, mes=mes_anterior).valor

    saldo_atual = saldo_mes_anterior + total_receber - total_pagar

    data = {
        'contas_pagar': list(map(lambda c: c.json(), contas_pagar)),
        'contas_receber': list(map(lambda c: c.json(), contas_receber)),
        'total_pagar': total_pagar,
        'total_receber': total_receber,
        'saldo_mes_anterior': saldo_mes_anterior,
        'saldo_atual': saldo_atual,
        'data_referencia': str(ano) + ' ' + meses[mes]
    }
    return render(request, 'fluxo_caixa_referencia.html', data)


def fluxo_caixa_processar():
    FluxoCaixa.objects.all().delete()
    ano = 2021
    meses = [7, 8, 9, 10, 11, 12]

    fluxo_caixa_criar(ano, 6, 15000)
    for mes in meses:
        saldo_mes_anterior = FluxoCaixa.objects.get(
            ano=ano, mes=mes - 1).valor
        contas_pagar = ContaPagar.objects.filter(
            data_vencimento__year=ano,
            data_vencimento__month=mes)
        contas_receber = ContaReceber.objects.filter(
            data_expectativa__year=ano,
            data_expectativa__month=mes)
        total_pagar = sum(c.valor for c in contas_pagar)
        total_receber = sum(c.valor for c in contas_receber)
        saldo_atual = saldo_mes_anterior + total_receber - total_pagar
        fluxo_caixa_criar(ano, mes, saldo_atual)


def fluxo_caixa_criar(ano, mes, valor):
    fluxo_caixa = FluxoCaixa()
    fluxo_caixa.ano = ano
    fluxo_caixa.mes = mes
    fluxo_caixa.valor = valor
    fluxo_caixa.save()
