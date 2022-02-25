from decimal import Decimal
from django.conf import settings

def favorites_contents(request):

    favorites_items = []
    total = 0
    product_count = 0


    context = {
        'favorites_items': favorites_items,
    }

    return context