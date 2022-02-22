from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    cart = request.session.get('cart', {})

    if color:
        if item_id in list(cart.keys()):
            if color in cart[item_id]['items_by_color'].keys():
                cart[item_id]['items_by_color'][color] += quantity
            else:
                cart[item_id]['items_by_color'][color] = quantity
        else:
            cart[item_id] = {'items_by_color': {color: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)  


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    color = None
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    cart = request.session.get('cart', {})

    if color:
        if quantity > 0:
            cart[item_id]['items_by_color'][color] = quantity
        else:
            del cart[item_id]['items_by_color'][color]
            if not cart[item_id]['items_by_color']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        color = None
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        cart = request.session.get('cart', {})

        if color:
            del cart[item_id]['items_by_color'][color]
            if not cart[item_id]['items_by_color']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)


        
