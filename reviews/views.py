from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
from reviews.forms import ReviewForm
from reviews.models import Reviews


def view_reviews(request):
    """ A view that renders the reviews contents page """

    return render(request, 'reviews/reviews.html')

def add_to_reviews(request,product_id):
    """ Add  the specified product to the shopping reviews """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.filter(product=product_id)

    form=ReviewForm(initial={'product': product})
    print(reviews, "Hello")
    context={"product":product,"form":form, "reviews":reviews}
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            product_id = product.id
            text = form.cleaned_data['text']
            rating = form.cleaned_data['rating']

            review =Reviews()
            review.product = product
            review.text = text
            review.rating = rating
            review.author = request.user
            review.save()

        return redirect(reverse('products'))
    return render(request,'reviews/review.html',context)






