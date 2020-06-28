import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelManager.settings')
import django
django.setup()

from modelManagerApp.models import *
from faker import Faker
from random import *

faker = Faker()
def populate(n):
    for i in range(n):
        fsno = randint(1001,9999)
        fsname = faker.name()
        fssal = randint(10000,20000)
        fsaddr = faker.city()
        stf_record= Staff.objects.get_or_create(sno = fsno,sname=fsname,ssal=fssal,saddr=fsaddr)
populate(20)
