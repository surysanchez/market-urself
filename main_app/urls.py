from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', view.about, name='about'),
    path('search/', views.search, name='search'),
    # shopping cart
    # checkout
    # item details
    # items edit/create
    # seller details
    # table details
    # table edit/create
    # profile details
    # profile edit/create

    path('',)
]