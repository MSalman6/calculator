from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
import requests
import json

def index(request):
	return render(request, 'index.html')

@api_view(['GET', 'POST'])
def calculator(request):
	r = request.POST['test']
	res = eval(r)
	print(res)
	return HttpResponse({'res':res}, content_type="text/plain")

def ajaxview(request):
	return render(request, 'ajax.html')