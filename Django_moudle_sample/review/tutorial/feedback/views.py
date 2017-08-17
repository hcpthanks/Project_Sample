from django.shortcuts import render
from django.http import HttpResponse
from .models import Feedback
from .forms import FeedbackForm

# Create your views here.


def home(request):
    context = {
        'categories': Feedback.CATEGORIES,
    }
    return render(request, 'feedback/feedback.html', context)


def feedback_form(request):
    form = FeedbackForm(initial={'subject':'反馈问题标题'})
    return render(request, 'feedback/feedback-form.html', {'form':form})



