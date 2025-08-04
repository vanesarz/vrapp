from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

def home(request):
    return HttpResponse("Halo dari halaman home trial!")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer