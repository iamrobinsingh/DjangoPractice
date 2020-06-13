from django.shortcuts import render

# Create your views here.

def page_count_view(request):
    count = request.session.get('count',0)
    newCount = count +1
    request.session['count']=newCount
    return render(request,'SessionApplication/count.html',{'count':newCount})
