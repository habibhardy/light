from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.


@csrf_exempt
def helloworld(request):
          return JsonResponse("Messege:Hello world :)" ,safe=False)

def helloApis(request):
          return JsonResponse("Messege:Hello API :) ! :)" ,safe=False)
                    
          
