from django.test import TestCase, Client

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    # Testing tambahan
    def test_title_web_ditampilkan(self):
        response = response = Client().get('/main/')
        self.assertContains(response,'- Pachill Market Stock Manager -')

    def test_deskripsi_ditampilkan(self):
        response = response = Client().get('/main/')
        self.assertContains(response,'Platform pengelola stok supermarket idaman kamu :D')