import unittest
from playstation import create_app, db
from playstation.models.users import User
from playstation.models.orders import Orders
from playstation.models.payments import Payments

class TestPaymentsModel(unittest.TestCase):
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
        self.order = Orders(
            user_id=self.user.id,
            total_amount=100.00,
            status="Pending"
        )
        self.order.save()
        self.payment_data = {
            "amount": 100,
            "order_id": self.order.id,
            "user_id": self.user.id,
            "payment_method": "Credit Card",
            "payment_status": "Completed",
            "currency": "$"
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_payment(self):
        payment = Payments(**self.payment_data)
        payment.save()
        self.assertIsNotNone(payment.id)
        self.assertEqual(payment.amount, self.payment_data["amount"])

    def test_update_payment(self):
        payment = Payments(**self.payment_data)
        payment.save()
        payment.payment_status = "Refunded"
        payment.save()
        updated_payment = Payments.query.get(payment.id)
        self.assertEqual(updated_payment.payment_status, "Refunded")

    def test_delete_payment(self):
        payment = Payments(**self.payment_data)
        payment.save()
        payment_id = payment.id
        payment.delete()
        deleted_payment = Payments.query.get(payment_id)
        self.assertIsNone(deleted_payment)

    def test_relationship_with_order_and_user(self):
        payment = Payments(**self.payment_data)
        payment.save()
        user = User.query.get(self.user.id)
        order = Orders.query.get(self.order.id)
        self.assertEqual(payment.user, user)
        self.assertEqual(payment.order, order)


if __name__ == '__main__':
    unittest.main()
