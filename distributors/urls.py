from django.urls import path
from distributors.views import *

urlpatterns = [
    path('', DistributorModelViewSet.as_view({'get': 'list'})),
    path('<int:id>/', DistributorDetailAPIView.as_view()),
    path('archive/<int:id>/', ArchiveDistributorView.as_view())
]

