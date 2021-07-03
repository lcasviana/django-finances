from django.http import HttpResponse, JsonResponse
from ..models import *

def contas_pagar_index(request):
    try:
        if request.method == 'GET':
            return contas_pagar_obtain_all(request)
        elif request.method == 'POST':
            return contas_pagar_insert(request)
        else:
            return HttpResponse(status=405)
    except Exception as e:
        return HttpResponse(status=500)

def contas_pagar_index_id(request, id):
    try:
        if request.method == 'GET':
            return contas_pagar_obtain_id(request, id)
        elif request.method == 'PUT':
            return contas_pagar_update(request, id)
        elif request.method == 'DELETE':
            return contas_pagar_delete(request, id)
        else:
            return HttpResponse(status=405)
    except Exception as e:
        return HttpResponse(status=500)

def contas_pagar_obtain_all(request):
    contas_pagar = ContaPagar.objects.all()
    resposta = { 'contas_pagar': list(map(lambda c: c.json(), contas_pagar)) }
    return JsonResponse(resposta, status=200)

def contas_pagar_insert(request):
    try:
        classificacao_obj = Classificacao.objects.find(descricao=classificacao).first()
    except Classificacao.DoesNotExist:
        return JsonResponse(resposta, status=200)

def contas_pagar_obtain_id(request, id):
    try:
        conta_pagar = ContaPagar.objects.get(id=id)
        resposta = conta_pagar.json()
        return JsonResponse(resposta, status=200)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)

def contas_pagar_update(request, id):
    try:
        conta_pagar = ContaPagar.objects.get(id=id)
        pass
        return HttpResponse(status=202)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)

def contas_pagar_delete(request, id):
    try:
        conta_pagar = ContaPagar.objects.get(id=id)
        conta_pagar.delete()
        return HttpResponse(status=200)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)
