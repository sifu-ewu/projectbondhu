import profile
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,Skill
from django.shortcuts import render
from .models import Question, Choice

from .models import Profile

# Create your views here.
def loginPage(request):
    page = 'register'
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User not found")
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('account')
        else :
            messages.error(request,"User/Password is error")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    messages.info(request,"User Logout")
    return redirect('login')
def registerUser(request):
    page = 'register'
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("profile")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        
    
    return render(request,"register.html",context={"register_form":form,"page":page})
@login_required(login_url='login')  
def profiles(request):
    profiles = Profile.objects.all()

    context = {"profiles":profiles}
   
    return render(request,'profiles.html',context)
@login_required(login_url='login')
def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request,'user-profile.html',context)
@login_required(login_url='login')
def userAccounts(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'account.html', context)
@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'profile_form.html',context)