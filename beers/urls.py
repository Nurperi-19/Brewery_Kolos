from django.urls import path
from beers.views import *

urlpatterns = [
    path('', BeerListView.as_view()),
    path('categories/', CategoryListView.as_view()),
]
