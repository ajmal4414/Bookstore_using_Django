import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect


from .models import Book, Order, Customer, Cart, Wishlist
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

class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            add=Customer.objects.get(pk=pk)
            add.name=form.cleaned_data['name']
            add.locality=form.cleaned_data['locality']
            add.city=form.cleaned_data['city']
            add.mobile=form.cleaned_data['mobile']
            add.state=form.cleaned_data['state']
            add.zipcode=form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulations! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')

# def add_to_cart(request):
#     user=request.user
#     product_id=request.GET.get('prod_id')
#     product=Book.objects.get(id=product_id)
#     Cart(user=user,product=product).save()
#     return redirect('addtocart')

# @login_required
# def add_to_cart(request, product_id):
#     user = request.user
#     product = Book.objects.get(id=product_id)
#     # Check if the user already has the item in their cart
#     cart_item, created = Book.objects.get(user=user, product=product)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return redirect('/cart')


def show_cart(request):
    user=request.user
    cart = Cart.objects.filter(user=user)
    return render(request,'addtocart.html',locals())


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



# add
# def view_cart(request):
#     if request.user.is_authenticated:
#         user = request.user
#         cart_items = Cart.objects.filter(user=user)
#         total_cost = sum(item.total_cost for item in cart_items)
#         context = {
#             'cart_items': cart_items,
#             'total_cost': total_cost,
#         }
#         return render(request, 'cart.html', context)
#     else:
#         # Redirect to the login page or handle anonymous user case
#         return redirect('login_page')  # Adjust the URL name to your login page


@login_required
def cart_view(request):
    # Retrieve the current user's cart items
    cart_items = Cart.objects.filter(user=request.user)

    return render(request, 'cart.html', {'cart_items': cart_items})



@login_required
def wishlist_view(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user)

    context = {
        'wishlist_items': wishlist_items
    }

    return render(request, 'wishlist.html', context)