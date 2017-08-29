from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def home(request):
     """首页vcard
     """
     return render(request, 'index.html')