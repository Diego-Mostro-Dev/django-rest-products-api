from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product


class UserTests(APITestCase):

    def test_create_user(self):
        url = "/api/users/"

        data = {
            "username": "juan",
            "password": "1234"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

class AuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="juan",
            password="1234"
        )

    def test_get_token(self):

        url = "/api/token/"

        data = {
            "username": "juan",
            "password": "1234"
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)


class ProductTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="juan",
            password="1234"
        )

        self.client.force_authenticate(user=self.user)

    def test_create_product(self):

        url = "/api/products/"

        data = {
            "name": "Laptop",
            "price": 1000
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)


class ProductPermissionTests(APITestCase):

    def setUp(self):

        self.user1 = User.objects.create_user("juan", password="1234")
        self.user2 = User.objects.create_user("ana", password="1234")

        self.product = Product.objects.create(
            name="Laptop",
            price=1000,
            owner=self.user1
        )

    def test_user_cannot_edit_other_product(self):

        self.client.force_authenticate(user=self.user2)

        url = f"/api/products/{self.product.id}/"

        data = {
            "name": "Hacked",
            "price": 500
        }

        response = self.client.put(url, data)

        self.assertEqual(response.status_code, 404)



class ProductListTests(APITestCase):

    def setUp(self):

        self.user1 = User.objects.create_user("juan", password="1234")
        self.user2 = User.objects.create_user("ana", password="1234")

        Product.objects.create(name="Laptop", price=1000, owner=self.user1)
        Product.objects.create(name="Mouse", price=50, owner=self.user2)

    def test_user_sees_only_his_products(self):

        self.client.force_authenticate(user=self.user1)

        response = self.client.get("/api/products/")

        self.assertEqual(response.status_code, 200)

        # solo debe devolver 1 producto
        self.assertEqual(len(response.data["results"]), 1)

        # verificar que sea el producto correcto
        self.assertEqual(response.data["results"][0]["name"], "Laptop")


class ProductFilterTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user("juan", password="1234")

        Product.objects.create(name="Laptop", price=1000, owner=self.user)
        Product.objects.create(name="Mouse", price=50, owner=self.user)
        Product.objects.create(name="Keyboard", price=150, owner=self.user)

        self.client.force_authenticate(user=self.user)

    def test_filter_by_min_price(self):

        response = self.client.get("/api/products/?min_price=100")

        self.assertEqual(response.status_code, 200)

        # deberían aparecer Laptop y Keyboard
        self.assertEqual(len(response.data["results"]), 2)

class ProductAuthTests(APITestCase):

    def test_unauthenticated_user_cannot_create_product(self):

        url = "/api/products/"

        data = {
            "name": "Laptop",
            "price": 1000
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 401)