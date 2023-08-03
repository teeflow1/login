from django.shortcuts import render, redirect
from blog.models import Able
from django.contrib import messages
from blog.forms import  UserAddForm

def home(request):
    
    good = Able.objects.all()
    
    return render(request, "blog/home.html", {'good':good})


def detail_record(request, pk):
    details = Able.objects.get(id=pk)
    return render(request, "blog/details.html", {'details':details})
    
    
def delete_record(request, pk):
    delete_it = Able.objects.get(id=pk)
    delete_it.delete()
    messages.success(request, "Your posy has been deleted successfully!!")
    return redirect('home')
    
def add_post(request):
    form = UserAddForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "You have submitted successfully!")
            return redirect('home')
    return render(request, "blog/add_post.html", {'form':form})


def update_record(request, pk):
    update_record = Able.objects.get(id=pk )
    form = UserAddForm(request.POST, instance=update_record)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Post have been updated successfully!")
        return redirect('home')
    return render(request, "blog/update_record.html", {'form':form})
        
         
    
   