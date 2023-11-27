from django.test import TestCase
from django.contrib.auth.models import User
from web_app.models import CustomUser


class GuestTest(TestCase):

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ingreso de")

    def test_register_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Registro de")

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        CustomUser.objects.create(id=self.user.id, name='testuser', points=0)

    def test_authenticated_access(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenid@")
