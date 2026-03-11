from ..models import Product


class ProductService:
  @staticmethod
  def get_products_for_user(user):
    return Product.objects.filter(owner=user)
