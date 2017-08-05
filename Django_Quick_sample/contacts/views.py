from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contact

# Create your views here.


def index(request):
    contact_list = Contact.objects.all()
    template = loader.get_template('contacts/index.html')
    context = {'contact_list': contact_list}
    return HttpResponse(template.render(context, request))


def detail(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    template = loader.get_template('contacts/detail.html')
    context = {'contact': contact}
    return HttpResponse(template.render(context, request))
