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
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            # data = dict(form.cleaned_data)
            # feedback = Feedback(**form.cleaned_data)
            # feedback.status = '待处理'
            # feedback.save()
            if request.FILES['screenshot']:
                upload_file(request.FILES['screenshot'])

            return redirect('/')
        # return HttpResponse('数据验证失败')
    return render(request, 'feedback/feedback-form.html', {'form':form})


def get_feedback_data(request):
    if request.method == 'GET':
        data = dict(request.GET)
        return HttpResponse(str(data))


#写入文件到本地硬盘
def upload_file(f):
    with open('uploads\{}'.format(f.name), 'wb+')as file:
        for chunk in f.chunks():
            file.write(chunk)
