from django.db import models
from django.contrib.auth.models import User

class Product (models.Model):
  name = models.CharField(max_length=200)
  price = models.PositiveIntegerField()
  owner = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='products')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
      return self.name
  
  class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"