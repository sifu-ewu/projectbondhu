from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/<str:pk>/',views.home,name="home"),
    path('project/<str:pk>/', views.Project, name="project"),

    path('create-project/', views.createProject, name="create-project"),

    path('update-project/<str:pk>/', views.updateProject, name="update-project"),

    path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
    path('doctors/',views.doctor_view,name="doctors"),
    path('doctor_profile/<str:pk>/',views.doctor_profile,name="doctor_profile"),
 
]
