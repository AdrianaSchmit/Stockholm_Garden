from django.shortcuts import render

# Create your views here.

def view_favorites(request):
    """ A view that renders the favorites contents page """

    return render(request, 'favorites/favorites.html')