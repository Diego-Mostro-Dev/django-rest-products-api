#Django
#Modelo User de Django
from django.contrib.auth.models import User
#DRF
#viewset de DRF
from rest_framework.viewsets import ModelViewSet
#Autenticacion y admin de DRF
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#Filtros de DRF 
from rest_framework.filters import SearchFilter, OrderingFilter
#Filtros personalizados
from .filters.product_filters import ProductFilter
#aca van los filtros tambien

# Third party
from django_filters.rest_framework import DjangoFilterBackend

#Local
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from .services.product_service import ProductService
from .permissions.product_permissions import IsOwnerOrReadOnly

#Healthcheck
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.db import connection


def db_health():
    try:
        connection.cursor().execute("SELECT 1")
        return True
    except:
        return False

START_TIME = datetime.datetime.utcnow()

@api_view(["GET"])
def health_check(request):
    uptime = datetime.datetime.utcnow() - START_TIME
    db_ok = db_health()
    return Response({
        "status": "ok",
        "uptime": str(uptime),  # ejemplo: "0:12:34.567890"
        "database": "connected" if db_ok else "error",
    })


class UserViewset(ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class ProductViewset(ModelViewSet):
  permission_classes = [IsAuthenticated , IsOwnerOrReadOnly]
  serializer_class = ProductSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

  search_fields = ["name"]
  filterset_class = ProductFilter
  ordering_fields = ["price", "name"]

  def get_queryset(self):
    #Cada usuario solo ve sus productos - importante ProductService porque es desde service
    return ProductService.get_products_for_user(self.request.user)

  #importante es perform no preform
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
  #Tiene que tener este queryset porque se queja django
  queryset = Product.objects.all()

class AdminProductViewset(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

