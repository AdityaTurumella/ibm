from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests
# Create your views here.
def Edit(request):

    return render(request, 'editor.html')

