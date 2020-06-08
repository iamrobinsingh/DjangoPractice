from django.shortcuts import render
from FilterApplication.models import FilterModel

# Create your views here.

def upper_view(request):
    data_list = FilterModel.objects.all()
    return render(request,'FilterApplication/upper.html',{'data_list':data_list})

def lower_view(request):
    data_list = FilterModel.objects.all()
    return render(request,'FilterApplication/lower.html',{'data_list':data_list})

def truncate_view(request):
    data_list = FilterModel.objects.all()
    return render(request,'FilterApplication/truncate.html',{'data_list':data_list})
