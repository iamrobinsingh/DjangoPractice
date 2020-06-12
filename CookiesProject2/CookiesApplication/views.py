from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request,'CookiesApplication/name.html')

def age_view(request):
    name= request.GET['name'] #reading data from name.html
    response = render(request,'CookiesApplication/age.html')
    response.set_cookie('name',name)
    return response

def address_view(request):
    age= request.GET['age'] #reading data from name.html
    response = render(request,'CookiesApplication/address.html')
    response.set_cookie('age',age)
    return response

def result_view(request):
    address = request.GET['address']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    response = render(request,'CookiesApplication/result.html',{'name':name,'age':age,'address':address})
    return response
