from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.


class UserTest(TestCase):
    def test_create_user(self):
        '''
            test user
        '''
        
        User = get_user_model()
        user = User.objects.create_user(email='test@example.com', password='a/123456')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="a/123456")

    def test_create_superuser(self): 
        '''
           test super user
        '''

        User = get_user_model() 
        admin_user = User.objects.create_superuser(email='test@example.com', password='a/123456')
        self.assertEqual(admin_user.email, 'test@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="test@example.com", password="a/123456", is_superuser=False)