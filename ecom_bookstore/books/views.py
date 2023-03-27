import json

from django.contrib import messages
from django.shortcuts import render,redirect


from .models import Book, Order, Customer
from django.views.generic import ListView, DetailView,View
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomerProfileForm
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

class ProflieView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request, 'profile.html', locals())
    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name=form.cleaned_data['name']
            locality= form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            reg= Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulations! Profile Save Successfully ")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,'profile.html',locals())

def address(request):
    add =Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

# class updateaddress(View):
#


class BookListView(ListView):
    model = Book
    template_name = 'list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'detail.html'

class BookCheckoutView(DetailView):
    model = Book
    template_name = 'checkout.html'

def PaymentComplete(request):
    body=json.loads(request.body)
    print('BODY:',body)
    product = Book.objects.get(id=body['productId'])
    Order.objects.create(product=product)
    return JsonResponse('payment completed', safe=False)


class SearchResultsView(ListView):
    model= Book
    template_name = 'search.html'

    def get_queryset(self):
        query=self.request.GET.get('q')
        return Book.objects.filter(Q(title=query) | Q(author=query))

