from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from rest_framework import viewsets
from .serializers import productSerializers

# Create your views here.



def Welcome(request):
    return HttpResponse('Welcome')

class productViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = productSerializers
