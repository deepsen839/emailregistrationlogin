import email
from statistics import fmean
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse

from .forms import registerUser,AuthenticationForm

# Create your views here.
def user_registration(request):
    form = registerUser(request.POST or None)
    
    if request.user.is_authenticated:
        redirect('/profile/')
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        #return HttpResponse(password)
        user = authenticate(email=email, password=password,backend='registeruser.backends.EmailAuthBackend')
        login(request, user,backend='registeruser.backends.EmailAuthBackend')
        return redirect('/')

    return render(request,'register/register.html', {'form': form})  

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('profile/')
    else:    
        
        if request.method=='POST':
            form = AuthenticationForm(data = request.POST)
            #return HttpResponse(request.POST['email'))
            if form.is_valid():
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email, password=password,backend='registeruser.backends.EmailAuthBackend')
                #return HttpResponse(user)
                login(request, user,backend='registeruser.backends.EmailAuthBackend')
                return redirect('/profile/')
        else:
            form = AuthenticationForm()  
        return render(request,'register/login.html',{'fm':form}) 

def profile(request):
     if request.user.is_authenticated:
        return render(request,'register/profile.html')
     else:
         return redirect('/login/')   
    