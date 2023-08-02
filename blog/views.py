from django.shortcuts import render
from blog.models import Able

def home(request):
    
    goods = Able.objects.all()
    
    return render(request, "blog/home.html", {'goods':goods})
