from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from .models import User


# Create your views here.
class ProfileView(View):
    def get(self, request):
        users = User.objects.get(username=request.user)
        contexto = {
            'user':users
        }
        return render(request,"users/profile_users.html", contexto)
        
        

class LoginView(View):
    def get(self, request):
        user_login = UserLoginForm()
        userform = UserRegisterForm()
        return render(request, "users/login_users.html",{'form':userform,'login_form':user_login})
    
    def post(self, request):
        if 'register_user' in request.POST:
            user_register = UserRegisterForm(request.POST)
            if user_register.is_valid():
                User.objects.create_user(username=user_register.cleaned_data.get("username"),
                                        email=user_register.cleaned_data.get("email"),
                                        password=user_register.cleaned_data.get("password"))
                return redirect('index')
        if 'login_user' in request.POST:
            login_form = UserLoginForm(request.POST)
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data.get("username"),
                                    password=login_form.cleaned_data.get("password"))
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("index")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('index')
