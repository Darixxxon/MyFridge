from django.contrib.auth.models import User
from django.test import TestCase
from .models import Fridge

class FridgeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="test123",
        )
        print(f"User {self.user.username} created")

        self.fridge = Fridge.objects.create(
            name="Test Fridge",
            owner=self.user
        )
        print(f"Fridge {self.fridge.name} created")

    def test_fridge_deleted_with_owner(self):
        self.user.delete()
        print(f"User {self.user.username} deleted")
        self.assertEqual(Fridge.objects.count(), 0)
        print("Fridge deleted cascade")
