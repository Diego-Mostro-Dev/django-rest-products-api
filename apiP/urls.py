from rest_framework.routers import DefaultRouter
from .views import UserViewset,ProductViewset, AdminProductViewset

router = DefaultRouter()
router.register(r'users' , UserViewset)
router.register(r'products',ProductViewset)
router.register(r'admin/products', AdminProductViewset, basename="admin-products")

urlpatterns = router.urls