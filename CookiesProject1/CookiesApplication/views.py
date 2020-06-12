from django.shortcuts import render

# Create your views here.
def count_views(request):
    count = int(request.COOKIES.get('count',0))
    newCount = count +1
    response = render(request,'CookiesApplication/count.html',context ={'count':newCount})
    response.set_cookie('count',newCount,max_age=60)
    return response
