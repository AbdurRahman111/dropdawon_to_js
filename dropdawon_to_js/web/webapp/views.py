from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import category
# Create your views here.
from django.core import serializers
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def index_1(request):
    print("i am here")
    r = request.POST.get('x')
    print(r)
    get_cat = category.objects.filter(name=r)
    print(get_cat)

    get_cat_seri = serializers.serialize('json', get_cat)
    return JsonResponse(get_cat_seri, safe=False)

