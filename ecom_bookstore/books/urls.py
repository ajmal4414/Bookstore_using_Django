from . import views
from .views import BookListView, BookDetailView,BookCheckoutView,PaymentComplete,SearchResultsView
from django.urls import path
urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

    path('profile/',views.ProflieView.as_view(),name='profile'),
    path('address/',views.address,name='address'),


    path('book_list',BookListView.as_view(),name='list'),
    path('details/<int:pk>/',BookDetailView.as_view(), name='detail-view'),
    path('checkout/<int:pk>/', BookCheckoutView.as_view(), name='checkout-view'),
    path('complete',PaymentComplete,name='complete'),
    path('search', SearchResultsView.as_view(), name='search'),
]