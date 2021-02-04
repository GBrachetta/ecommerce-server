from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Product
from .serializers import ProductSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        data["username"] = self.user.username
        data["email"] = self.user.email

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def getRoutes(request):
    """ summary """

    routes = [
        "/api/products/",
        "/api/products/create/",
        "/api/products/upload/",
        "/api/products/<id>/reviews/",
        "/api/products/top/",
        "/api/products/<id>/",
        "/api/products/delete/<id>/",
        "/api/products/<update>/<id>/",
    ]
    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    """ summary """

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, pk):
    """ summary """

    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
