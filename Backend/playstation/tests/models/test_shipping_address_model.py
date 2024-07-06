import unittest
from playstation import create_app, db
from playstation.models.users import User
from playstation.models.shipping_address import ShippingAddress

class TestShippingAddressModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User.create_user(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            password="password123"
        )
        self.address_data = {
            "user_id": self.user.id,
            "address": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "country": "AnyCountry",
            "default": True
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_shipping_address(self):
        address = ShippingAddress(**self.address_data)
        address.save()
        self.assertIsNotNone(address.id)
        self.assertEqual(address.city, self.address_data["city"])

    def test_update_shipping_address(self):
        address = ShippingAddress(**self.address_data)
        address.save()
        address.city = "New City"
        address.save()
        updated_address = ShippingAddress.query.get(address.id)
        self.assertEqual(updated_address.city, "New City")

    def test_delete_shipping_address(self):
        address = ShippingAddress(**self.address_data)
        address.save()
        address_id = address.id
        address.delete()
        deleted_address = ShippingAddress.query.get(address_id)
        self.assertIsNone(deleted_address)

    def test_relationship_with_user(self):
        address = ShippingAddress(**self.address_data)
        address.save()
        user = User.query.get(self.user.id)
        self.assertIn(address, user.shipping_addresses)


if __name__ == '__main__':
    unittest.main()
