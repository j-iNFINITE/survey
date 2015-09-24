from django.shortcuts import render
from django.http import HttpResponse
from survey.models import answers
# Create your views here.
def index(request):
    return render(request,'index.html')
def search(request):
    return render(request,'search.html')
def done(request):
    isdone = request.GET['isdone']
    SN = request.GET['SN']
    content = answers.objects.get(SN=SN)
    content.isdone=isdone
    content.save()
    return render(request,'done.html')
def form(request):
    context_dict={}
    SN = request.GET['sn']
    try:
        content = answers.objects.get(SN=SN)
        context_dict['SN']=content.SN
        context_dict['iszong']=content.iszong
        context_dict['iscredit']=content.iscredit
        context_dict['isbaobei']=content.isbaobei
        context_dict['isdone']=content.isdone
    except answers.DoesNotExist:
        context_dict['error']='输入的客户编号有误'
        return render(request,'search.html',context_dict)
    if content.isdone is not None:
        context_dict['error']='该户问卷已填写，不允许修改'
        return render(request,'search.html',context_dict)
    return render(request,'form.html',context_dict)