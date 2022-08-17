from distutils.command.config import config
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,doctor
from .forms import ProjectForm

# Create your views here.


def index(request):
    data = Project.objects.all()
    return render(request,'index.html',{'data':data})

def home(request,pk):
 items = Project.objects.get(id=pk)
 tags=items.tags.all()
        
 return render(request,'home.html',{'items':items, 'tags':tags})

def createProject(request):
    form =ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context ={'form':form}
    return render(request,'project_form.html',context)
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    
    form =ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('index')


    context ={'form':form}

    return render(request,'project_form.html',context)
def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
      project.delete()
      return redirect('index')  
    context ={'object':project}
    return render(request,'delete_object.html',context)

def doctor_view(request):
    data = doctor.objects.all()
    return render(request,'projects.html',{'data':data})

def doctor_profile(request,pk):
 data = doctor.objects.get(id=pk)
 return render(request,'single-project.html',{'data':data})