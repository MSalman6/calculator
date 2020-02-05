from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from math import cos, sin, tan, sqrt


def index(request):
	return render(request, 'index.html')


@api_view(['GET', 'POST'])
def calculator(request):
		r = request.POST['input']
		data = eval(r)
		return HttpResponse(data)