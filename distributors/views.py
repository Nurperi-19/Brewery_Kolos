from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from distributors.models import *
from distributors.serializers import *


class DistributorModelViewSet(ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    lookup_field = 'id'

class DistributorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    lookup_field = 'id'

class ArchiveDistributorView(generics.UpdateAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    def perform_update(self, serializer):
        serializer.save(archived=True)

