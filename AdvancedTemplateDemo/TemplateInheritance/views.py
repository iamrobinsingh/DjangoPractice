from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'TemplateInheritance/home.html')

def movies_view(request):
    return render(request,'TemplateInheritance/movies.html')

def sports_view(request):
    return render(request,'TemplateInheritance/sports.html')

def politics_view(request):
    return render(request,'TemplateInheritance/politics.html')
