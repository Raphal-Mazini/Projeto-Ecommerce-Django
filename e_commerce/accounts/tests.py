from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.email = "teste@exemplo.com"
        self.password = "senha123"
        self.user = User.objects.create_superuser(email=self.email, password=self.password)

    def test_login_redirect_next(self):
        target_url = '/cart/checkout/'
        url_com_next = f"{reverse('login')}?next={target_url}"
        
        # O 'next' no dicionário simula o preenchimento do campo hidden pelo navegador
        response = self.client.post(url_com_next, {
            'email': self.email,
            'password': self.password,
            'next': target_url 
        }, follow=True)
        
        self.assertRedirects(response, target_url)