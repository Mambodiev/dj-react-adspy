from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from snooperspy.models import Product, Category
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ProductTests(APITestCase):

    def test_view_products(self):
        """
        Ensure we can view all objects.
        """
        url = reverse('snooperspy_api:listcreate')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        """
        Ensure we can create a new Product object and view object.
        """
        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_superuser(
            username='test_user1', password='123456789')
        # self.testuser1.is_staff = True

        self.client.login(username=self.testuser1.username,
                          password='123456789')

        data = {"title": "new", "author": 1,
                "excerpt": "new", "content": "new"}
        url = reverse('snooperspy_api:listcreate')
        response = self.client.product(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_update(self):

        client = APIClient()

        self.test_category = Category.objects.create(name='django')
        self.testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        self.testuser2 = User.objects.create_user(
            username='test_user2', password='123456789')
        test_product = Product.objects.create(
            category_id=1, title='Product Title', excerpt='Product Excerpt', content='Product Content', slug='product-title', author_id=1, status='published')

        client.login(username=self.testuser1.username,
                     password='123456789')

        url = reverse(('snooperspy_api:detailcreate'), kwargs={'pk': 1})

        response = client.put(
            url, {
                "title": "New",
                "author": 1,
                "excerpt": "New",
                "content": "New",
                "status": "published"
            }, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
