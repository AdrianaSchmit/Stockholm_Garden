from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_reviews, name='view_reviews'),
    path('add_to_reviews/<int:product_id>', views.add_to_reviews, name='add_to_reviews'),

] 