from django.shortcuts import render
from django.http import HttpResponse
from survey.models import answers
# Create your views here.
def index(request):
    return render(request,'index.html')
def search(request):
    return render(request,'search.html')
def done(request):
    sn = request.GET['sn']
    content = answers.objects.get(SN=sn)
    content.Q_version=request.GET['Qversion']
    content.Q_overbank=request.GET['Qoverbank']
    content.Q_iscredit=request.GET['Qcredit']
    content.Q_baobei=request.GET['Qbaobei']
    content.Q1_most=request.GET['most']
    content.Q2_choice=request.GET['Q2']
    content.Q2_text=request.GET['Q2text']
    content.hly = request.GET['hly']
    content.name = request.GET['name']
    content.sex = request.GET['sex']
    content.phone = request.GET['phone']
    content.isdone=True
    content.save()
    return render(request,'done.html')
def form(request):
    context_dict={}
    SN = request.GET['sn']
    try:
        content = answers.objects.get(SN=SN)
        context_dict['SN']=content.SN
        if len(context_dict['SN'])<18:
            context_dict['ver']='省行版'
        else:
            context_dict['ver']='总行版'
            context_dict['isver']='hidden'
        context_dict['m_name']= content.m_name
        context_dict['m_phone']= content.m_phone
        context_dict['m_address']= content.m_address
        context_dict['isoverbank'] = content.isoverbank
        print(content.isoverbank)
        context_dict['iscredit']=content.iscredit
        context_dict['isbaobei']=content.isbaobei
        context_dict['islow']=content.islow
        context_dict['isdone']=content.isdone
        context_dict['isoverbankhidden']=''
        context_dict['iscredithidden']=''
        context_dict['isbaobeihidden']=''
        for i in context_dict:
            if i == 'isoverbank' or i=='iscredit' or i =='isbaobei':
                if context_dict[i]:
                    context_dict[i+'hidden']='hidden'
                else:
                    context_dict[i+'hidden']=''
            if context_dict[i]==True:
                context_dict[i]='是'
            if context_dict[i]==False:
                context_dict[i]='否'
    except answers.DoesNotExist:
        context_dict['error']='输入的客户编号有误'
        return render(request,'search.html',context_dict)
    if content.isdone is True:
        context_dict['error']='该户问卷已填写，不允许修改'
        return render(request,'search.html',context_dict)
    return render(request,'form.html',context_dict)