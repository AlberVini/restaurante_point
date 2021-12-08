from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView
from django.contrib import messages
#from django.core.paginator import Paginator

from foods.models import Product
from users.models import Restaurant, User, Client
from .forms import EditClientForm, AddProductRestaurantForm, EditRestaurantForm
from orders.models import Order, Item


class AboutPageView(TemplateView):
    template_name = 'registration/about.html'

def home_page(request):

    return render(request, 'home.html')

def client_setup(request):
    user = get_object_or_404(User, username=request.user)
    client = get_object_or_404(Client, user_id=user.client.user_id)
    

    context = {'user': user,
        'client':client
    }
    return render(request, 'pages/client_setup.html', context)

def edit_client(request):
    client = get_object_or_404(Client, user_id=request.user.client.user_id)

    form = EditClientForm(request.POST or None, request.FILES or None, instance=client)

    if request.method == 'POST':
        form = EditClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            return redirect('pages:client_setup')
        else:
            return render(request, 'pages/edit_client.html', {'form': form, 'client': client})
    else:
        return render(request, 'pages/edit_client.html', {'form': form, 'client': client})

def get_restaurant(id):
    obj = get_object_or_404(Restaurant, user_id=id)
    return obj

def restaurant_setup(request):
    restaurant = get_restaurant(request.user.restaurant.user_id)
    context = {'restaurant': restaurant}
    return render(request, 'pages/restaurant_setup.html', context)

def add_product(request):
    form = AddProductRestaurantForm()
    
    restaurant = get_restaurant(request.user.restaurant.user_id)

    if request.method == 'POST':
        form = AddProductRestaurantForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.restaurante = restaurant
            new_product.save()

            return redirect('pages:restaurant_setup')
        else:
            return render(request, 'pages/addproduct_restaurant.html', {'form':form, 'restaurant': restaurant})
    return render(request, 'pages/addproduct_restaurant.html', {'form': form, 'restaurant': restaurant})

def edit_restaurant(request):
    restaurant_edit = get_restaurant(request.user.restaurant.user_id)
    user = get_object_or_404(User, username=request.user)

    form = EditRestaurantForm(instance=restaurant_edit)

    if request.method == 'POST':
        form = EditRestaurantForm(request.POST or None, request.FILES or None, instance=restaurant_edit)
        
        if form.is_valid():
            restaurant_form = form.save(commit=False)
            restaurant_form.user = user
            restaurant_form.save()

            return redirect('pages:restaurant_setup')
        else:
            return render(request, 'pages/edit_restaurant.html', {'form': form, 'restaurant': restaurant_edit})
    
    return render(request, 'pages/edit_restaurant.html', {'form': form, 'restaurant': restaurant_edit})

def list_product(request):
    restaurant = get_restaurant(request.user.restaurant.user_id)
    products = Product.objects.filter(restaurante=restaurant)

    return render(request, 'pages/products_restaurant.html', {'products': products, 'restaurant':restaurant})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()

    #messages.info(request, f'{product.nome} deletado(a)')
    messages.warning(request, f'{product.nome} deletado(a)')

    return redirect('pages:list_product')

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    restaurant_product = get_restaurant(request.user.restaurant.user_id)

    form = AddProductRestaurantForm(instance=product)
    if request.method == 'POST':
        form = AddProductRestaurantForm(request.POST or None, request.FILES or None, instance=product)

        if form.is_valid():
            edit_form = form.save(commit=False)

            edit_form.restaurante = restaurant_product
            edit_form.save()
            
            return redirect('pages:list_product')
        else:
            return render(request, 'pages/edit_product.html', {'form': form, 'product': product, 'restaurant': restaurant_product})
            
    return render(request, 'pages/edit_product.html', {'form': form, 'product': product, 'restaurant': restaurant_product})


class ListOrders(ListView):
    template_name = 'pages/orders_client.html'

    def get_queryset(self):
        
        queryset = Order.objects.filter(user_id=self.request.user.id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tot_price'] = {}

        for values in context['object_list']:
            tot = 0
            for item in values.items.all():
                tot += (item.price * item.quantity)

            context['tot_price'][values.id] = str(tot)

        return context


def restaurant_orders(request):

    restaurant = get_restaurant(request.user.restaurant.user_id)
    
    products = list(restaurant.restaurante.values_list("id"))

    orders = Order.objects.filter(items__product_id__in=products).distinct()
    
    context = {'orders': orders}

    return render(request, 'pages/orders_restaurant.html', context)

