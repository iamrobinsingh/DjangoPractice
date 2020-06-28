from django.shortcuts import render
from modelManagerApp.models import Staff

# Create your views here.
def retrive_view(request):
    #staff = Staff.objects.all()
    staff = Staff.objects.get_stf_sal_range(12000,17000) # own define Custom Manager Method
    return render(request,'modelManagerApp/index.html',{'staff':staff})
