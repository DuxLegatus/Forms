from django.shortcuts import render,redirect,get_object_or_404
from .models import Users
from .forms import *
# Create your views here.


def show_all_users(request):
    users = Users.objects.all()
    return render(request,"users/all_user.html",{"users":users})


def show_specific_user(request,pk):
    user = get_object_or_404(Users,pk=pk)
    return render(request,"users/one_user.html",{"user":user})


def delete_user(request,pk):
    user = get_object_or_404(Users,pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect("all_user")
    return render(request, 'users/delete_page.html', {'user': user})

def add_user(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_user")
    else:
        form = UsersForm()
    return render(request, 'users/add_page.html', {'form': form})


def update_user(request,pk):
    user = get_object_or_404(Users,pk=pk)
    if request.method == "POST":
        form = UsersForm(request.POST,instance=user)
        form.save()
        return redirect("all_user")
    else:
        form = UsersForm(instance=user)
    return render(request, 'users/update_page.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return redirect('thank_you')
        
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'contact/thank_you.html')

