from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import TableForm, ItemForm
from .models import Table, Item, Profile
# from .models import Profile, Categories, Table, Photo, Item, Order, Review


# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def search(request):
  return render(request, 'search.html')

def cart(request):
  return render(request, 'cart.html')
  
def checkout(request):
  return render(request, 'checkout.html')

def category(request):
  absPath = request.path
  category = absPath.replace('/', '')
  items = Item.objects.filter(category = category)
  return render(request, 'category/detail.html', {'category': category, 'items': items})

def items_detail(request, pk):
  table = Table.objects.filter(user=request.user)
  item = Item.objects.get(id=pk)
  return render(request, 'items/detail.html', {'item': item})

def tables_detail(request, pk):
  table = Table.objects.get(id= pk)
  items = Item.objects.filter(table=table)
  return render(request, 'main_app/table_detail.html', {'table': table, 'items': items})

def category(request):
  absPath = request.path
  category = absPath.replace('/', '')
  return render(request, 'category/detail.html', {'category': category})

def profiles_detail(request):
  profile = Profile.objects.get(user=request.user)
  try:
    table = Table.objects.get(user=request.user)
  except:
    table = None
  
  return render(request, 'profiles/detail.html', {'profile': profile, 'table': table})
  

class ItemCreate(CreateView):
  model = Item
  fields = ['item_name', 'item_price', 'item_description', 'category']
  success_url = '/profiles/details/'

  def form_valid(self, form):
    form.instance.table = Table.objects.get(user=self.request.user)
    return super().form_valid(form)

class ItemUpdate(UpdateView):
  model = Item
  fields = ['item_name', 'item_price','item_desciption']

class ItemDelete(DeleteView):
  model = Item
  success_url = '/'


class TableDetail(DetailView):
  model = Table


class TableCreate(CreateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category']
  success_url = '/profiles/details/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TableUpdate(UpdateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category']
  success_url = '/profiles/details/'
  
class TableDelete(DeleteView):
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
  fields = ['first_name', 'address']

class ProfileDelete(DeleteView):
  pass
  
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