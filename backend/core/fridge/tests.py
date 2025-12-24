from django.contrib.auth.models import User
from django.test import TestCase
from .models import Fridge

class FridgeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test123",
        )

        self.fridge = Fridge.objects.create(
            name="Test Fridge",
            owner=self.user
        )

    def test_fridge_deleted_with_owner(self):
        self.user.delete()
        self.assertEqual(Fridge.objects.count(), 0)
