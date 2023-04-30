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

def items_detail(request):
  items = Item.objects.filter(user=request.user)
  return render(request, 'items/detail.html', {'items': items})

def tables_detail(request):
  tables = Table.objects.filter(user=request.user)
  return render(request, 'tables/detail.html', {'tables': tables})

def profiles_detail(request):

  return render(request, 'profiles/detail.html')


class ItemCreate(CreateView):
  model = Item
  fields = ['table', 'item_name', 'item_price', 'item_description', 'category']

  def form_valid(self, form):
    form.instance.user = self.request.user # set the user
    return super().form_valid(form)

class ItemUpdate(UpdateView):
  model = Item
  fields = '__all__'

class ItemDelete(DeleteView):
  model = Item
  success_url = '/tables/tables_details.html'

class TableCreate(CreateView):
  model = Table
  fields = ['table_name', 'table_description', 'table_category']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  
class TableUpdate(UpdateView):
  model = Table
  fields = '__all__'
  
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
  pass

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