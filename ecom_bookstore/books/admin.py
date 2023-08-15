from django.contrib import admin
from .models import Book, Customer, Cart,Wishlist

# Register your models here.
admin.site.register(Book)

admin.site.register(Customer)

admin.site.register(Cart)

admin.site.register(Wishlist)