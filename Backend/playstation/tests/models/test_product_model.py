import unittest
from playstation import create_app, db
from playstation.models.products import Product, Category

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.category = Category(name="Electronics")
        self.category.save()
        self.product_data = {
            "name": "Smartphone",
            "description": "Latest model",
            "price": 699.99,
            "stock": 50,
            "category_id": self.category.id
        }

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_product(self):
        product: Product = Product(**self.product_data)
        product.save()
        self.assertIsNotNone(product.id)
        self.assertEqual(product.name, self.product_data["name"])

    def test_update_product(self):
        product: Product = Product(**self.product_data)
        product.save()
        product.price = 649.99
        product.save()
        updated_product: Product = Product.query.get(product.id)
        self.assertEqual(updated_product.price, 649.99)

    def test_delete_product(self):
        product = Product(**self.product_data)
        product.save()
        product_id = product.id
        product.delete()
        deleted_product = Product.query.get(product_id)
        self.assertIsNone(deleted_product)

    def test_relationship_with_category(self):
        product: Product = Product(**self.product_data)
        product.save()
        category: Category = Category.query.get(self.category.id)
        self.assertIn(product, category.products)


if __name__ == '__main__':
    unittest.main()
