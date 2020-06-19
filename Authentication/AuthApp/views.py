from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AuthApp.forms import SignUpForm
from django.http import  HttpResponse,HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'AuthApp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'AuthApp/javaExam.html')

@login_required
def python_exam_view(request):
    return render(request,'AuthApp/pythonExam.html')

@login_required
def aptitude_exam_view(request):
    return render(request,'AuthApp/aptitudeExam.html')

def logout_view(request):
    return render(request,'AuthApp/logout.html')

def sign_up_view(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'AuthApp/signup.html',{'form':form})
