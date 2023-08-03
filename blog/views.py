from django.shortcuts import render
from blog.models import Able

def home(request):
    
    good = Able.objects.all()
    
    return render(request, "blog/home.html", {'good':good})
