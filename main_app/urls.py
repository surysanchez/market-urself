from django.urls import path
from . import views

urlpatterns = [
    # django sign up
    path('accounts/signup/', views.signup, name='signup'),

    # home / landing page
    path('', views.home, name='home'),

    # about page
    path('about/', views.about, name='about'),

    # search bar result page
    path('search/', views.search, name='search'),

    # shopping cart
    path('cart/', views.cart, name='cart'),

    # checkout
    path('checkout/', views.checkout, name='checkout'),

    # item details
    path('items/', views.items_detail, name='items_detail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),

    # table details
    path('tables/', views.tables_detail, name='tables_detail'),
    path('tables/create/', views.TableCreate.as_view(), name='tables_create'),
    path('tables/<int:pk>/update/', views.TableUpdate.as_view(), name='tables_update'),
    path('tables/<int:pk>/delete/', views.TableDelete.as_view(), name='tables_delete'),

    # profile details
    path('profiles/detail/', views.profiles_detail, name='profiles_detail'),
    # path('profiles/create', views.ProfilesCreate.as_view(), 
    path('profiles/<int:profiles_id>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:profiles_id>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
]