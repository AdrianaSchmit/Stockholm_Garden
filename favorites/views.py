from django.shortcuts import render, redirect

# Create your views here.

def view_favorites(request):
    """ A view that renders the favorites contents page """

    return render(request, 'favorites/favorites.html')

def add_to_favorites(request, item_id):
    """ Add  the specified product to the shopping favorites """

    redirect_url = request.POST.get('redirect_url')
    favorites = request.session.get('favorites', {})

    request.session['favorites'] = favorites
    print(request.session['favorites'])
    return redirect(redirect_url)