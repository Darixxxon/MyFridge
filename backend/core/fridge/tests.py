from decimal import Decimal

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Fridge, Product


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

    def test_fridge_is_deleted_with_owner(self):
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

class ProductModelTest(TestCase):
    def setUp(self):
        self.product_data = {
            "name": "Test Product",
            "brand": "Test Brand",
            "measurement": Decimal("1.00"),
            "unit": "l",
            "barcode": "1234567890123",
        }

    def test_create_valid_product(self):
        product = Product(**self.product_data)
        product.full_clean()
        product.save()
        self.assertEqual(Product.objects.count(), 1)

    def test_delete_product(self):
        product = Product.objects.create(**self.product_data)
        product.delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_measurement_must_be_positive(self):
        product = Product(**self.product_data)
        product.measurement = Decimal("0.01")
        product.full_clean()

    def test_measurement_cannot_be_nonpositive(self):
        product = Product(**self.product_data)
        product.measurement = Decimal("0")
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_name_required(self):
        product = Product(**self.product_data)
        product.name = ""
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_unit_required(self):
        product = Product(**self.product_data)
        product.unit = ""
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_barcode_required(self):
        product = Product(**self.product_data)
        product.barcode = ""
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_valid_unit(self):
        product = Product(**self.product_data)
        product.unit = "invalid unit"
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_barcode_unique(self):
        Product.objects.create(**self.product_data)
        product2 = Product(**self.product_data)
        with self.assertRaises(ValidationError):
            product2.full_clean()

    def test_product_str(self):
        product = Product.objects.create(**self.product_data)
        self.assertEqual(str(product), "Product Test Product with barcode 1234567890123")
