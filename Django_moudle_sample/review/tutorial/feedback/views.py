from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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


def feedback_list(request):
    """信息列表页"""
    q = request.GET.get('q', '')
    items = Feedback.objects.filter(subject__contains=q).order_by('-posted_time')
    return render(request, 'feedback/feedback-list.html', {'items':items})


def feedback_editor(request,fid):
    # feedback = Feedback.objects.get(pk=fid)
    feedback = get_object_or_404(Feedback, pk=fid)
    return render(request, 'feedback/feedback-editor.html', {'item': feedback})


def feedback_edit(request, fid):
    fb = get_object_or_404(Feedback, pk=fid)
    form = FeedbackForm(initial={
        'subject': fb.subject,
        'category': fb.category,
        'username': fb.username,
        'email': fb.email,
        'description': fb.description,
        'subscription': fb.subscription,
        'status': fb.status,
        'posted_time': fb.posted_time,
    })
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            for k, v in form.cleaned_data.items():
                setattr(fb, k, v)
            fb.save()
            return redirect(reverse('feedback:feedback_list'))
    return render(request, 'feedback/feedback-edit.html', {'form':form})


def feedback_delete(request,fid):
    fd = get_object_or_404(Feedback, pk=fid)
    fd.delete()
    return redirect(reverse('feedback:feedback_list'))


