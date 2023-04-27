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
    # table details
    path('tables/<int:table_id>/', views.tables_detail, name='tables_detail'),
    # table edit/create
    path('tables/create/', views.TableCreate.as_view(), name='tables_create'),
    path('tables/<int:pk>/update/', views.TableUpdate.as_view(), name='tables_update'),
    path('tables/<int:pk>/delete/', views.TableDelete.as_view(), name='tables_delete'),

    # public profile details view
    path('users/<int:profiles_id>/', views.profiles_detail, name='users_detail'),
    # path('profiles/create', views.ProfilesCreate.as_view(), name='profiles_create'),

    # private user profile details
    # profile edit/create
    path('users/<int:profiles_id>/update', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('users/<int:profiles_id>/delete', views.ProfileDelete.as_view(), name='profiles_delete'),
]