import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abcsite.settings')
import django
django.setup()
from survey.models import answers
def add(sn,m_name,m_address,m_phone,isoverbank,iscredit,isbaobei,islow):
    c = answers.objects.get_or_create(SN=sn,m_name=m_name,m_address=m_address,m_phone=m_phone,isoverbank=isoverbank,iscredit=iscredit,isbaobei=isbaobei,islow=islow,isdone=False)
    # c[0].m_name = line[1]
    # c[0].m_address = line[2]
    # c[0].m_phone = line[3]
    # c[0].isoverbank = line[4]
    # c[0].iscredit = line [5]
    # c[0].isbaobei = line[6]
    # c[0].islow = line[7]
    # c[0].isdone=False
    # c.save()
    return c
f = open('pu.csv','r',encoding='utf-8')
lines = f.readlines()
i = 1
for line in lines:
    if i == 1:
        i+=1
        continue
    line = line.split('	')
    for li in range(4,8):
        line[li]=line[li].strip()
        if line[li] =='FALSE' or line[li]=='NULL':
            line[li]=''
    add(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7].strip())
    print(i)
    i+=1
