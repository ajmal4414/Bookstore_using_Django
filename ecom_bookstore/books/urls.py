from . import views
from .views import BookListView, BookDetailView,BookCheckoutView,PaymentComplete,SearchResultsView
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('profile/',views.ProflieView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(), name='updateAddress'),
    # path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    # add on 29
    # path('view_cart/<int:product_id>',views.view_cart,name='view_cart'),
    # add on 7-8
    path('view_cart/',views.cart_view,name='cart_view'),
    path('showcart/',views.show_cart,name='showcart'),
#     wishlist
    path('wish_list/',views.wishlist_view,name='wishlist_view'),
#     temprry prpse
#     path('checkout/',views.show_cart,name='checkout'),


    path('book_list',BookListView.as_view(),name='list'),
    path('details/<int:pk>/',BookDetailView.as_view(), name='detail-view'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout-view'),
    path('complete',PaymentComplete,name='complete'),
    path('search', SearchResultsView.as_view(), name='search'),
]