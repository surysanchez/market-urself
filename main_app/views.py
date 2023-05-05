from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import TableForm, ItemForm, ReviewForm
from .models import Table, Item, Profile, Cart, CartItem, Review

# from .models import Profile, Categories, Table, Photo, Item, Order, Review


# Create your views here.

def home(request):
  items = Item.objects.all()
  featured_table = Table.objects.get(id=1)
  user = request.user
  return render(request, 'home.html', {'items':items, 'featured_table': featured_table, 'user': user})

def about(request):
  return render(request, 'about.html')

def search(request):
  query2 = request.GET.get('q')
  results = Item.objects.filter(item_name__icontains=query2)
  searchedStr = query2
  
  return render(request, 'search.html', {'results':results, 'searchedStr': searchedStr})

@login_required
def cart(request):
  cart = Cart.objects.get(user=request.user)
  items = CartItem.objects.filter(cart = cart)
  return render(request, 'cart.html', {'cart': cart, 'items': items})
  
@login_required
def checkout(request):
  profile = Profile.objects.get(user=request.user)
  return render(request, 'checkout.html', {'profile': profile})

def clear_cart(request):
  cart = Cart.objects.get(user=request.user)
  CartItem.objects.filter(cart = cart).delete()
  return redirect('/')

def category(request):
  absPath = request.path
  category = absPath.replace('/', '')
  items = Item.objects.filter(category = category)
  return render(request, 'category/detail.html', {'category': category, 'items': items})


def items_detail(request, pk):
  item = Item.objects.get(id=pk)
  request.session['cur_item'] = item.item_name
  reviews = Review.objects.filter(item=item)
  if request.user.is_authenticated:
    userA = True
  else:
    userA = False
  print(request.user)
  is_user = False
  if item.table.user == request.user:
    is_user = True
  else:
    is_user = False
  return render(request, 'items/detail.html', {'item': item, 'is_user':is_user, 'reviews':reviews, 'userA':userA})

def tables_detail(request, pk):
  table = Table.objects.get(id= pk)

  if table.user == request.user:
    is_user = True
  else:
    is_user = False

  items = Item.objects.filter(table=table)

  return render(request, 'tables/detail.html', {'table': table, 'items': items, 'is_user': is_user})


def profiles_detail(request, pk):
  profile = Profile.objects.get(id=pk)
  if profile.user == request.user:
    is_user = True
  else:
    is_user = False

  try:
    table = Table.objects.get(user=request.user)
  except:
    table = None
    
  return render(request, 'profiles/detail.html', {'profile': profile, 'table': table, 'is_user':is_user})

def clear_cart(request):
  cart = Cart.objects.get(user=request.user)
  CartItem.objects.filter(cart = cart).delete()
  return redirect('/')

class ItemCreate(CreateView):
  model = Item
  fields = ['item_name', 'item_price', 'item_description', 'category', 'image']

  def form_valid(self, form):
    table = Table.objects.get(user=self.request.user)
    form.instance.table = table
    # success_url = '/tables/{table.id}/'
    return super().form_valid(form)

class CartItemCreate(CreateView):
  model = CartItem
  fields = ['quantity']
  success_url = '/cart/'

  def form_valid(self, form):
    form.instance.cart = Cart.objects.get(user=self.request.user)
    cur_name = self.request.session['cur_item']
    form.instance.item = Item.objects.get(item_name=cur_name)
    return super().form_valid(form)

class CartItemDelete(LoginRequiredMixin, DeleteView):
  model = CartItem
  success_url = '/'

class ItemUpdate(LoginRequiredMixin, UpdateView):
  model = Item
  fields = ['item_name', 'item_price','item_description', 'image', 'category']

class ItemDelete(LoginRequiredMixin, DeleteView):
  model = Item
  success_url = '/'


class TableDetail(DetailView):
  model = Table


class TableCreate(LoginRequiredMixin, CreateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category', 'image']
  success_url = '/managers/detail/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TableUpdate(LoginRequiredMixin, UpdateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category', 'image']
  success_url = '/managers/detail/'
  
class TableDelete(LoginRequiredMixin, DeleteView):
  model = Table
  success_url = '/managers/detail/'

# Public profile details view
# def profiles_detail(request):
#   return render(request, 'profiles/detail', )
  # profile = Profile.objects.get('profile_id': profile_id)
  # # Need to identify what "username" is by connecting profile_id to it's user
  # if request.user.username == username:
  #   pass
  #   return render(request, 'profiles/detail.html')
  # else:
  #   return render(request, 'different.html')

## DON'T USE THIS AT THIS POINT
# Private user profile view
# def users_detail(request, profile_id):
#   return render(request, 'users/detail.html')

class ProfileCreate(CreateView):
  model = Profile
  fields = ['first_name', 'last_name', 'address', 'city', 'zip', 'state', 'birthday', 'about']

  def form_valid(self, form):
    form.instance.user = self.request.user
    Cart.objects.create(user=self.request.user)
    return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['first_name', 'last_name', 'address', 'city', 'zip']

class ProfileDelete(DeleteView):
  pass


class ManagerCreate(CreateView):
  model = Profile
  fields = ['first_name', 'last_name', 'address', 'city', 'zip', 'state', 'birthday', 'about']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ManagerUpdate(UpdateView):
  model = Profile
  fields = ['first_name', 'last_name', 'address']

class ManagerDelete(DeleteView):
  pass
  
def managers_detail(request):
  profile = Profile.objects.get(user=request.user)
  try:
    table = Table.objects.get(user=request.user)
  except:
    table = None
  items = Item.objects.filter(table=table)
  return render(request, 'managers/detail.html', {'profile': profile, 'table': table, 'items': items})
  

# auth 
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('profiles_create')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


## Item Reviews WIP
class ReviewsList(TemplateView):
  model = Review 

class ReviewsDetail(ListView):
  model = Review
  
class ReviewsCreate(CreateView):
  model = Review 
  fields = ['item_rating', 'comment']
  success_url = '/'
 

  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.item = Item.objects.get(item_name=self.request.session['cur_item'] )
    return super().form_valid(form)
  
class ReviewsDelete(DeleteView):
  model = Review 
  success_url = '/'

