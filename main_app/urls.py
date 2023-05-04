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
    path('cartitems/create/', views.CartItemCreate.as_view(), name='cart_items_create'),
    path('cartitems/<int:pk>/delete/', views.CartItemDelete.as_view(), name='cart_item_delete'),


    # checkout
    path('checkout/', views.checkout, name='checkout'),
    path('clearCart/', views.clear_cart, name ='clear_cart'),

    # item details
    path('items/', views.items_detail, name='items_detail'),
    path('items/<int:pk>/', views.items_detail, name='items_detail'),    
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),

    #items reviews
    path('reviews/', views.ReviewsList.as_view(), name='reviews_item'),
    path('reviews/<int:pk>', views.ReviewsDetail.as_view(), name='reviews_detail'),
    path('reviews/create/', views.ReviewsCreate.as_view(), name='reviews_create'),
    path('reviews/<int:pk>/delete/', views.ReviewsDelete.as_view(), name='reviews_delete'),

   
    # table details
    path('tables/<int:pk>/', views.tables_detail, name='tables_detail'),
    path('tables/create/', views.TableCreate.as_view(), name='tables_create'),
    path('tables/<int:pk>/update/', views.TableUpdate.as_view(), name='tables_update'),
    path('tables/<int:pk>/delete/', views.TableDelete.as_view(), name='tables_delete'),

    # profile details
    path('profiles/<int:pk>/', views.profiles_detail, name='profiles_detail'),
    path('profiles/create/', views.ProfileCreate.as_view(), name='profiles_create'), 
    path('profiles/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profiles_update'),
    path('profiles/<int:pk>/delete/', views.ProfileDelete.as_view(), name='profiles_delete'),
    
    # managers details
    path('managers/detail/', views.managers_detail, name='managers_detail'),
    path('managers/create/', views.ManagerCreate.as_view(), name='managers_create'), 
    path('managers/<int:pk>/update/', views.ManagerUpdate.as_view(), name='managers_update'),
    path('managers/<int:pk>/delete/', views.ManagerDelete.as_view(), name='managers_delete'),

    #categories
    path('wearables', views.category, name='category_detail'),
    path('homeables', views.category, name='category_detail'),
    path('gardenables', views.category, name='category_detail'),
    path('entertainables', views.category, name='category_detail'),
    path('consumables', views.category, name='category_detail'),
    path('miscellaneous', views.category, name='category_detail'),
]