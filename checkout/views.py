from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KWhPyGjivoOTbjHoi9OJUJgXRW9VoXwAvv1SIRk91Myuet1dBJbDp7EQQMtLML3cfTzRaXIhBiIlBpz2LmGy9OB008be3kQLy',
        'client_secret': 'sk_test_51KWhPyGjivoOTbjHmCHZwei7NmeznGMuAVdEF1WZIyu1Y11UrVFLFhja2QyuEvb9qP8eSJ4IV8uIilb8vJmLoeTo00ceyRNEVY',
    }

    return render(request, template, context)