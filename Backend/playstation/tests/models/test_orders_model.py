import unittest
from datetime import datetime
from playstation import create_app, db
from playstation.models.users import User
from playstation.models.orders import Orders
from playstation.models.products import Product, Category
from playstation.models.shipping_address import ShippingAddress
from playstation.models.coupons import Coupons

class TestOrdersModel(unittest.TestCase):
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
        self.category = Category(name="Electronics")
        self.category.save()
        self.product = Product(
            name="Smartphone",
            description="Latest model",
            price=699.99,
            stock=50,
            category_id=self.category.id
        )
        self.product.save()
        self.address = ShippingAddress(
            user_id=self.user.id,
            address="123 Main St",
            city="Anytown",
            state="Anystate",
            country="AnyCountry",
            default=True
        )
        self.address.save()
        self.coupon = Coupons(
            code="DISCOUNT10",
            discount=10.0,
            expiration_date= datetime.strptime('2024-12-31', '%Y-%m-%d').date()
        )
        self.coupon.save()
        self.order_data = {
            "user_id": self.user.id,
            "shipping_address_id": self.address.id,
            "coupon_id": self.coupon.id,
            "total_amount": 629.99,
            "status": "Pending"
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_order(self):
        order = Orders(**self.order_data)
        order.save()
        self.assertIsNotNone(order.id)
        self.assertEqual(order.total_amount, self.order_data["total_amount"])

    def test_update_order(self):
        order = Orders(**self.order_data)
        order.save()
        order.status = "Shipped"
        order.save()
        updated_order = Orders.query.get(order.id)
        self.assertEqual(updated_order.status, "Shipped")

    def test_delete_order(self):
        order = Orders(**self.order_data)
        order.save()
        order_id = order.id
        order.delete()
        deleted_order = Orders.query.get(order_id)
        self.assertIsNone(deleted_order)

    def test_relationship_with_user_shipping_address_coupon_product(self):
        order = Orders(**self.order_data)
        order.products.append(self.product)
        order.save()
        user = User.query.get(self.user.id)
        address = ShippingAddress.query.get(self.address.id)
        coupon = Coupons.query.get(self.coupon.id)
        self.assertEqual(order.user, user)
        self.assertEqual(order.shipping_address, address)
        self.assertEqual(order.coupon, coupon)
        self.assertIn(self.product, order.products)


if __name__ == '__main__':
    unittest.main()
