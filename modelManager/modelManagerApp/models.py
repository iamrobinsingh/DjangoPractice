from django.db import models

# Create your models here.
class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(ssal__gte=15000)

    def get_stf_sal_range(self,ssal1,ssal2): # own function acc to our need
        return super().get_queryset().filter(ssal__range=(ssal1,ssal2)).order_by('sno')


class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('sname')


class Staff(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length =64)
    ssal = models.FloatField()
    saddr = models.CharField(max_length = 256)

    objects = CustomManager1() # object for custom manager

class ProxyStaff(Staff): # Proxy Inheritance
    objects = CustomManager2()
    class Meta:
        proxy=True
# You can define as many proxy class you want you jst need a customModelManager to create distinct view
