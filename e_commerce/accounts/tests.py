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
        # Usamos o reverse para pegar a URL exata configurada no sistema
        target_url = reverse('cart:checkout') # Isso retornará '/cart/checkout/'
        login_url = reverse('login')
        url_com_next = f"{login_url}?next={target_url}"
        
        # Simulamos o login passando o destino
        response = self.client.post(url_com_next, {
            'email': self.email,
            'password': self.password,
            'next': target_url 
        }, follow=True)
        
        # Agora o assert deve encontrar a correspondência exata
        self.assertRedirects(response, target_url)