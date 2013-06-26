from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

def rootview(request):
    return render_to_response(
            'editing-inline.html',
            {
            },
            RequestContext(request)
        )

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from grid.models import Products
from grid.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics


class ProductList(viewsets.ModelViewSet):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    """


