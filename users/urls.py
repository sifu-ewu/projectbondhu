from django.urls import path
from . import views
urlpatterns = [

    path('',views.profiles,name="profile"),
    path('loginPage/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name='register'),
    path('profile/',views.profiles,name="profile"),
    path('userprofile/<str:pk>/',views.userProfile,name="userprofile"),
    path('account/',views.userAccounts,name="account"),
    path('edit-account/',views.editAccount,name="editAccount"),

]