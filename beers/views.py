from rest_framework import generics
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import BeerFilter

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BeerListView(generics.ListAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BeerFilter

