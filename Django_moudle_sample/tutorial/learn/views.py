from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import reverse
from django.template import Template, Context

# Create your views here.


def home(request):
    return HttpResponse('优品课堂 django课程')


def rsp_attr(request):
    """手动构造响应"""
    rsp = HttpResponse(content='django 教程', content_type='text/html', charset='utf8')
    rsp.content = 'web 全栈'
    rsp.write('django 网站开发')
    rsp.writelines(['aaa', 'bbb', 'ccc'])
    rsp.flush()
    return rsp


def rsp_redirect(request):
    """
    响应转跳
    :param request:
    :return:
    """
    rsp = HttpResponseRedirect(reverse('learn:home'))
    return rsp


def rsp_json(request):
    """
    响应JSON
    :param request:
    :return:
    """
    import datetime
    emp = {'name': 'hcpthanks', 'age': 20, 'birtadate': datetime.date(1990, 3, 3)}
    rsp = JsonResponse(emp)
    return rsp


def rsp_header(request):
    """
    自定义响应头部
    :param request:
    :return:
    """
    rsp = HttpResponse('自定义头部信息')
    rsp['age'] = 20
    # del rsp['age']
    return rsp


def rsp_download(request):
    """
    作为附件下载
    :param request:
    :return:
    """
    f = open('static/data.txt', 'r', encoding='utf8')
    rsp = HttpResponse(content=f, content_type='application/force-download')
    rsp['Content-Disposition'] = 'attachment;filename=readme.txt'
    return rsp


def tmp_loading(request):
    """
    载入模板
    :param request:
    :return:
    """
    # template = Template('当前课程是:{{ course_title }}')
    # context = Context({'course_title': 'django web开发'})
    # return HttpResponse(template.render(context), request)

    from django.template import loader
    # context = Context({'course_title': 'django web 开发'})
    # template = loader.get_template('tmp-1.html')
    # # template = loader.select_template('tmp-1.html')
    # return HttpResponse(template.render(context, request))

    return HttpResponse(loader.render_to_string('tmp-1.html', {'course_title': 'python django'}, request))

def tmp_render(request):
    """
    响应跳转
    :param request:
    :return:
    """
    return render(request, 'tmp-1.html', {'course_title':'web 全栈开发'})


def tmp_article(request):
    return render(request, 'article.html')


