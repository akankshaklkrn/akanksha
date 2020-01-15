from django.shortcuts import render
from django.http import HttpResponse
from .models import Gift,user

# Create your views here.
def index(req):
    return render(req,'home/landing_page.html')

def admin_login(req):
    return render(req,'home/admin_login.html')

def add_gifts(req):
    if req.method=='POST':
        add_gifts=Gift(
            image=req.POST.get('image'),
            description=req.POST.get('description'),
            quantity=req.POST.get('quantity') 
        )
        add_gifts.save()
        return HttpResponse('Gift Added')
    else:
      # return render(req,'home/add_gifts.html',{'data':'random'})
        return render(req,'home/add_gifts.html')

def select_gift(req):
    gifts=Gift.objects.all()             
    return render(req,'home/select_gift.html',{'gifts':gifts})

def form(req):
    if req.method=='POST':
        form=user(
            username=req.POST.get('username'),
            mob_no=req.POST.get('mob_no'),
            address=req.POST.get('address'),
            description=req.gifts
        )
        form.save()
        return HttpResponse('Gift Added')
    else:
        return render(req,'home/form.html')

def view_selected_gifts(req):
    users=user.objects.all()
    return render(req,'home/view_selected_gifts.html',{'users':users})

def final(req):
    return render(req,'home/final.html')