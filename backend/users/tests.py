from django.test import TestCase
from users.models import CustomUser

class CustomUserCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(first_name="Sri Harsha", last_name="G", email="ghant.sriharsha@gmail.com")
    
    def test_user_fetch(self):
        user = CustomUser.objects.get(first_name = "Sri Harsha")
        self.assertEqual(user.get_short_name(), "G")
    
    # def test_user_fetch_last_name(self):
    #     user = CustomUser.objects.get(last_name = "G")
    #     self.assertEqual(user.first_name, "Sri Harsha")
    
    # def test_multiple_user_fetch(self):
    #     CustomUser.objects.create(first_name="Sri Harsha", last_name="G dash", email="ghant.sriharsha@gmail.com")
        # user = CustomUser.objects.get(first_name = "Sri Harsha")
        # self.assertEqual(user.last_name, "G")
    
    # def test_user_email_blank(self):
    #     user = CustomUser.objects.get(first_name = "Sri Harsha")