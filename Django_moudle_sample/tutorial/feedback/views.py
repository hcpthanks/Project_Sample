from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback

# Create your views here.


def home(request):
    context = {
        'categories': Feedback.CATEGORIES,
    }
    return render(request, 'feedback/feedback.html', context)
