from django import urls
from django.urls import path
from  .import views
from .views import SignUpView


urlpatterns=[
    path('signup/',SignUpView.as_view(),name='sign-up'),
    # path('login/',views.login_fun,name='login')

]