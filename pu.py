import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abcsite.settings')
import django
django.setup()
from survey.models import answers
def add(sn):
    c = answers.objects.get(SN=sn)
    c.isdone=True
    return c
add('190071335864693000')
