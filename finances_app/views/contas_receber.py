from django.http import JsonResponse
from ..models import *

def contas_receber_index(request):
    try:
        if request.method == 'GET':
            return contas_receber_obtain_all(request)
        elif request.method == 'POST':
            return contas_receber_insert(request)
        else:
            return JsonResponse(status=405)
    except Exception as e:
        return JsonResponse(str(e), status=500)

def contas_receber_index_id(request, id):
    try:
        if request.method == 'GET':
            return contas_receber_obtain_id(request, id)
        elif request.method == 'PUT':
            return contas_receber_update(request, id)
        elif request.method == 'DELETE':
            return contas_receber_delete(request, id)
        else:
            return JsonResponse(status=405)
    except Exception as e:
        return JsonResponse(str(e), status=500)

def contas_receber_obtain_all(request):
    contas_receber = ContaReceber.objects.all()
    resposta = { 'contas_receber': list(map(lambda c: c.json(), contas_receber)) }
    return JsonResponse(resposta, status=200)

def contas_receber_insert(request):
    pass

def contas_receber_obtain_id(request, id):
    try:
        conta_receber = ContaReceber.objects.get(id=id)
        resposta = conta_receber.json()
        return JsonResponse(resposta, status=200)
    except ContaReceber.DoesNotExist:
        return HttpResponse(status=404)

def contas_receber_update(request, id):
    try:
        conta_receber = ContaReceber.objects.get(id=id)
        pass
        return HttpResponse(status=202)
    except ContaReceber.DoesNotExist:
        return HttpResponse(status=404)

def contas_receber_delete(request, id):
    try:
        conta_receber = ContaReceber.objects.get(id=id)
        conta_receber.delete()
        return HttpResponse(status=200)
    except ContaPagar.DoesNotExist:
        return HttpResponse(status=404)
