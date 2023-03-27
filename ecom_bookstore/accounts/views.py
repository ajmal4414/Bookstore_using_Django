from django.shortcuts import render,redirect
# from .forms import RegisterForm, LoginForm
from .models import  Register,Login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

#
# def register_fun(request):
#     register=Register.objects.all()
#     form=RegisterForm()
#
#     if request.method=='POST':
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         context={'register':register,'form':form}
#         return render(request,'register.html',context)
#
#
#
#
# def login_fun(request):
#     login=Login.objects.all()
#     form=LoginForm()
#
#
#     if request.method == 'POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#         context ={'login': login,'form':form}
#         return render(request,'login.html',context)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'