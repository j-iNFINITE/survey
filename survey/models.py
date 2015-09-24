from django.db import models

# Create your models here.
class answers(models.Model):
    SN = models.CharField(max_length=18,primary_key=True)
    iszong = models.NullBooleanField(null=True)
    iscredit = models.NullBooleanField(null=True)
    isbaobei = models.NullBooleanField(null=True)
    most = models.IntegerField(null=True)
    isdone = models.NullBooleanField(null=True)
    def __str__(self):
        return self.SN
