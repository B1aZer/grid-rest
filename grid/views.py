from django.template import RequestContext
from django.shortcuts import render_to_response

from rest_framework import status, mixins, viewsets, generics
from rest_framework.response import Response

from grid.models import Products, Shop
from grid.serializers import ProductSerializer, ShopSerializer

def rootview(request):
    return render_to_response(
            'editing-inline.html',
            {
            },
            RequestContext(request)
        )


class ProductList(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    generics.GenericAPIView):
    """
    reasssignin create method (post) for shop addition
    """

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Filter by shop
        """
        queryset = Products.objects.all()
        shop = self.request.QUERY_PARAMS.get('shopid', None)
        if shop is not None:
            queryset = queryset.filter(shop__id=shop)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.object.shop = Shop.objects.get(id = request.DATA.get('shop_id',1))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    def pre_save(self, obj):
        shop = Shop.objects.get(id = 1)
        obj.shop = shop
    """

class ProductChange(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


