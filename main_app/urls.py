from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    # shopping cart
    path('cart/', views.cart, name='cart'),
    # checkout
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    # item details
    path('items/<int:item_id>/', views.items_detail, name='items_detail'),
    # items edit/create
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
    # public profile details view
    path('profile/<int:profiles_id>/', views.profiles_detail, name='profiles_detail'),
     # table edit/create
    path('profiles/create', views.ProfilesCreate.as_view(), name='profiles_create'),
    path('tables/<int:table_id>/', views.tables_detail, name='tables_detail'),
    # table details
    path('tables/create/', views.TableCreate.as_view(), name='tables_create'),
    path('tables/<int:pk>/update/', views.TableUpdate.as_view(), name='tables_update'),
    path('tables/<int:pk>/delete/', views.TableDelete.as_view(), name='tables_delete'),
    # private user profile details
    path('users/', views.users_detail, name='users_detail'),
    # profile edit/create
   
    path('users/<int:profiles_id>/update', views.ProfilesUpdate.as_view(), name='profiles_update'),
    path('users/<int:profiles_id>/delete', views.ProfilesDelete.as_view(), name='profiles_delete'),

     
]