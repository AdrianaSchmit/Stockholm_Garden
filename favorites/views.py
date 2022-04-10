from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_favorites(request):
    """ A view that renders the favorites contents page """

    return render(request, 'favorites/favorites.html')

def add_to_favorites(request, item_id):
    """ Add  the specified product to the shopping favorites """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})
    favorites[item_id] = {item_id:item_id,
    "name":product.name,
    "price":str(product.price)}
    request.session['favorites'] = favorites
    return redirect(redirect_url)

def remove_from_favorites(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})

    if favorites.pop(item_id, None) is not None:
        messages.success(request, f'Removed {product.name} from your favorites')

    request.session['favorites'] = favorites
    return redirect(view_favorites) 
       
