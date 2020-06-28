from django.db import models

# Create your models here.
# Abstract Base class model inheritance
class ContactInfo(models.Model):
    name= models.CharField(max_length =128)
    email = models.EmailField()
    addr = models.CharField(max_length =128)
    class Meta:
        abstract = True

class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher(ContactInfo):
    subject = models.CharField(max_length = 128)
    salary = models.FloatField()


# Multi Table model inheritance
class ContactInfos(models.Model):
    name= models.CharField(max_length =128)
    email = models.EmailField()
    addr = models.CharField(max_length =128)


class Student1(ContactInfos):
    rollno = models.IntegerField()
    marks = models.IntegerField()

class Teacher1(ContactInfos):
    subject = models.CharField(max_length = 128)
    salary = models.FloatField()


#Multi-level Inheritance
class Parent(models.Model):
    prop1 = models.CharField(max_length = 128)
    prop2 = models.CharField(max_length = 128)

class Child(Parent):
    prop3 = models.CharField(max_length = 128)
    prop4 = models.CharField(max_length = 128)

class SubChild(Child):
    prop5 = models.CharField(max_length = 128)


#Proxy-Model Inheritance
 #--> Check in customModelManagerProject 
