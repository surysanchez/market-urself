from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TableForm, ItemForm, ReviewForm
from .models import Table, Item, Profile, Cart, CartItem, Review

# from .models import Profile, Categories, Table, Photo, Item, Order, Review


# Create your views here.

def home(request):
  items = Item.objects.all()
  return render(request, 'home.html', {'items':items})

def about(request):
  return render(request, 'about.html')

def search(request):
  # query = Item.objects.get(item_name='Pot2')
  query2 = request.GET.get('q')
  # print(query2)
  # print(request.GET)
  results = Item.objects.filter(item_name__contains=query2)
  
  return render(request, 'search.html', {'results':results})

def cart(request):
  cart = Cart.objects.get(user=request.user)
  items = CartItem.objects.filter(cart = cart)
  return render(request, 'cart.html', {'cart': cart, 'items': items})
  
def checkout(request):
  return render(request, 'checkout.html')

def category(request):
  absPath = request.path
  category = absPath.replace('/', '')
  items = Item.objects.filter(category = category)
  return render(request, 'category/detail.html', {'category': category, 'items': items})


def items_detail(request, pk):
  item = Item.objects.get(id=pk)
  request.session['cur_item'] = item.item_name
  reviews = Review.objects.filter(item=item)
  is_user = False
  if item.table.user == request.user:
    is_user = True
  else:
    is_user = False
  return render(request, 'items/detail.html', {'item': item, 'is_user':is_user, 'reviews':reviews})

def tables_detail(request, pk):
  table = Table.objects.get(id= pk)
  items = Item.objects.filter(table=table)
  return render(request, 'main_app/table_detail.html', {'table': table, 'items': items})

def profiles_detail(request):
  profile = Profile.objects.get(user=request.user)
  try:
    table = Table.objects.get(user=request.user)
  except:
    table = None
  return render(request, 'profiles/detail.html', {'profile': profile, 'table': table})
  

class ItemCreate(CreateView):
  model = Item
  fields = ['item_name', 'item_price', 'item_description', 'category', 'image']
  success_url = '/profiles/details/'

  def form_valid(self, form):
    form.instance.table = Table.objects.get(user=self.request.user)
    return super().form_valid(form)

class CartItemCreate(CreateView):
  model = CartItem
  fields = '__all__'
  success_url = '/'
  def form_valid(self, form):
    # item = 
    item = Item.objects.get(item_name = self.request.session['cur_item'])
    form.item = item
    form.quantity = 1
    print('idiot ')
    print(item)
    return super().form_valid(form)

  # form_valid(x, y)


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
  success_url = '/profiles/details/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TableUpdate(LoginRequiredMixin, UpdateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category', 'image']
  success_url = '/profiles/details/'
  
class TableDelete(LoginRequiredMixin, DeleteView):
  model = Table
  success_url = '/'

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
    return super().form_valid(form)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = ['first_name', 'last_name', 'address']

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
  return render(request, 'managers/detail.html', {'profile': profile, 'table': table})
  

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

