from django.shortcuts import render, redirect
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
    form = FeedbackForm({'status': '未处理'})
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # data = dict(form.cleaned_data)
            feedback = Feedback(**form.cleaned_data)
            feedback.status = '待处理'
            feedback.save()
            return redirect('/')
        # return HttpResponse('数据验证失败')
    return render(request, 'feedback/feedback-form.html', {'form':form})



