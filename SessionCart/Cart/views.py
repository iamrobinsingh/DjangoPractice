from django.shortcuts import render
from Cart.forms import AddItemForms

# Create your views here.
def add_item_view(request):
    form = AddItemForms()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(60)
    return render (request,'Cart/additem.html',{'form':form})

def display_item_view(request):
    return render(request,'Cart/displayItem.html')

def session_info_view(request):
    session = request.session
    age = session.get_expiry_age()
    date = session.get_expiry_date()

    return render(request,'Cart/sessionInfo.html',{'age':age,'date':date})
