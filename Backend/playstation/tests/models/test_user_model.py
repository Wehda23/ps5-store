import unittest
from playstation import create_app, db
from playstation.models.users import User
from playstation.models.blacklisted_tokens import BlackListedTokens
from playstation.models.exceptions import ExistingEmail

class TestUserModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_user(self):
        user = User.create_user(**self.user_data)
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, self.user_data["email"])

    def test_update_user(self):
        user = User.create_user(**self.user_data)
        user.first_name = "Jane"
        user.save()
        updated_user = User.query.get(user.id)
        self.assertEqual(updated_user.first_name, "Jane")

    def test_delete_user(self):
        user = User.create_user(**self.user_data)
        user_id = user.id
        user.delete()
        deleted_user = User.query.get(user_id)
        self.assertIsNone(deleted_user)

    def test_duplicate_email(self):
        User.create_user(**self.user_data)
        with self.assertRaises(ExistingEmail):
            User.create_user(**self.user_data)


if __name__ == '__main__':
    unittest.main()
