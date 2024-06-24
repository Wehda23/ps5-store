# Serializer Package

This package provides a framework for creating serializers in a Python application. It includes abstract base classes for defining the serialization process and concrete implementations that can be used to serialize models.

## Folder Structure

```txt
project_root/
    playstation/
        serializers/
            __init__.py
            serializer.py
```

## Contents

### `serializer.py`

This file contains the abstract classes and their methods for implementing serializers. The main abstract class is `AbstractSerializer`, which defines the basic structure for serializers. Other abstract classes such as `Validatable`, `Saveable`, `Updatable`, `Deletable`, `Representable`, `Creatable`, and `ToInstance` provide additional functionality for managing model instances.

### `__init__.py`

This file imports the necessary classes from `serializer.py` and defines concrete implementations of serializers such as `SerializerInterface`, `Serializer`, and `ModelSerializer`.

## Usage

### Creating a Serializer

To create a serializer for a model, you need to define a subclass of `ModelSerializer` and specify the model and fields in the `Meta` class.

#### Example

```python
# serializers.py

from playstation import serializers
from playstation.models.products import Product, Category

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "stock", "category_id", "image_url"]
```

### Using the Serializer

You can use the serializer to serialize and deserialize data. Here are some examples:

#### Serializing Data

```py
# Get all categories
categories = Category.query.all()
serializer = CategorySerializer(categories, many=True)
print(serializer.data)
```

#### Deserializing Data

```python
# Create a new product
data = {
    "name": "New Product",
    "price": 100,
    "description": "A new product description",
    "stock": 10,
    "category_id": 1,
    "image_url": "http://example.com/image.png"
}
serializer = ProductSerializer(data=data)
if serializer.is_valid():
    product = serializer.save()
    print(product.id)
else:
    print(serializer.errors)
```

#### Updating a Product

```python
# Update an existing product
product = Product.query.get(1)
data = {
    "name": "Updated Product",
    "price": 120,
    "description": "Updated description",
    "stock": 15
}
serializer = ProductSerializer(instance=product, data=data)
if serializer.is_valid():
    updated_product = serializer.save()
    print(updated_product.name)
else:
    print(serializer.errors)
```

#### Deleting a Product

```python
# Delete a product
product = Product.query.get(1)
serializer = ProductSerializer(instance=product)
serializer.delete()
```

## Validators

You can also add custom validation methods in the serializer class. Here is an example:

```python
class CreateProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "category_id", "image_url"]

    def validate_name(self, value):
        if len(value) < 3:
            raise ValueError("Name should be at least 3 characters long.")
        return value
```

## Error Handling

If there are validation errors, they will be available in the `errors` property of the serializer:

```python
if not serializer.is_valid():
    print(serializer.errors)
```

## Conclusion

This serializer package provides a flexible way to handle serialization and deserialization of models in your Python application. You can extend and customize the serializers as needed for your specific use cases.