from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_reviews(request):
    """ A view that renders the reviews contents page """

    return render(request, 'reviews/reviews.html')

def add_to_reviews(request, item_id):
    """ Add  the specified product to the shopping reviews """
    product_review = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    reviews = request.session.get('reviews', {})
    reviews[item_id] = {item_id:item_id,
    request.session['reviews'] = reviews
    return redirect(redirect_url)
    

