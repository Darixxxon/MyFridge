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

    def test_fridge_create(self):
        self.assertEqual(Fridge.objects.count(), 1)

    def test_fridge_deleted_with_owner(self):
        self.user.delete()
        self.assertEqual(Fridge.objects.count(), 0)

    def test_fridge_delete(self):
        self.fridge.delete()
        self.assertEqual(Fridge.objects.count(), 0)

    def test_fridge_name(self):
        self.assertEqual(self.fridge.name, "Test Fridge")

    def test_fridge_description(self):
        self.assertEqual(self.fridge.description, "")

    def test_fridge_owner(self):
        self.assertEqual(self.fridge.owner, self.user)

    def test_fridge_str(self):
        self.assertEqual(
            str(self.fridge),
            "Fridge Test Fridge"
        )
