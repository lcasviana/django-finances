from django.shortcuts import render
from django.http import HttpResponse
from ..models import *


def index(request):
    contas_pagar = ContaPagar.objects.all()
    contas_receber = ContaReceber.objects.all()
    data = {
        'contas_pagar': list(map(lambda c: c.json(), contas_pagar)),
        'contas_receber': list(map(lambda c: c.json(), contas_receber)),
    }
    return render(request, 'index.html', data)
