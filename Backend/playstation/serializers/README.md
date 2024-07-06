# Serializer Module for Flask Application

This module provides a set of serializers for your Flask application, allowing you to easily validate and serialize data. The serializers are built with flexibility and extendability in mind, providing features such as nested serialization and integration with Pydantic models.

## Installation

To use the serializers in your project, simply include the necessary files in your application directory.

## Usage

### Basic Usage

Here's an example of how to use the `UserRegisterSerializer` to validate and create a new user:

```python
from your_application.serializers import UserRegisterSerializer
from your_application.models import User

data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword123"
}

serializer = UserRegisterSerializer(data=data)
if serializer.is_valid():
    user = serializer.save()
    print("User created:", user)
else:
    print("Errors:", serializer.errors)
```

### Nested Serialization

To handle nested relationships, you can define nested serializers and use them in your main serializer. 

#### Single Nested Object

When dealing with a single nested object, you do not need to specify `many=True`. Here's an example:

```python
from your_application.serializers import UserSerializer, ShippingAddressSerializer

class UserDetailSerializer(UserSerializer):
    shipping_address = ShippingAddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'shipping_address']

# Usage
user = User.query.get(1)
serializer = UserDetailSerializer(instance=user)
print(serializer.data)
```

This will serialize the `shipping_address` field as a dictionary:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "shipping_address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zipcode": "12345"
    }
}
```

#### Multiple Nested Objects

When dealing with multiple nested objects, use `many=True` to return a list of dictionaries. Here's an example:

```python
from your_application.serializers import UserSerializer, ShippingAddressSerializer

class UserDetailSerializer(UserSerializer):
    shipping_addresses = ShippingAddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'shipping_addresses']

# Usage
user = User.query.get(1)
serializer = UserDetailSerializer(instance=user)
print(serializer.data)
```

This will serialize the `shipping_addresses` field as a list of dictionaries:

```json
{
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "shipping_addresses": [
        {
            "street": "123 Main St",
            "city": "Anytown",
            "zipcode": "12345"
        },
        {
            "street": "456 Elm St",
            "city": "Othertown",
            "zipcode": "67890"
        }
    ]
}
```

### Integration with Pydantic Models

You can also integrate Pydantic models for additional validation. Here's an example:

```python
from your_application.serializers import UserSerializer
from pydantic import BaseModel, EmailStr, ValidationError

class UserPydanticModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class UserPydanticSerializer(UserSerializer):
    pydantic_model = UserPydanticModel

    def validate_pydantic(self, data):
        try:
            pydantic_instance = self.pydantic_model(**data)
            return pydantic_instance.model_dump()  # Dump the validated model to dictionary
        except ValidationError as e:
            raise SerializerError(e, "Invalid data")

# Usage
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}

serializer = UserPydanticSerializer(data=data)
if serializer.is_valid():
    print("Valid data:", serializer.validated_data)
else:
    print("Errors:", serializer.errors)
```

### Updating Existing Instances

The `.save()` method is designed to update an instance if it already exists, rather than creating a new one. If the `instance` attribute is set, `.save()` will call the `.update()` method. If `instance` is `None`, it will call `.create()`.

Here's an example:

```python
from your_application.serializers import UserSerializer
from your_application.models import User

# Update an existing user
user_instance = User.query.get(1)
data = {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
}

serializer = UserSerializer(instance=user_instance, data=data)
if serializer.is_valid():
    user = serializer.save()
    print("User updated:", user)
else:
    print("Errors:", serializer.errors)
```

## Custom Serializers

You can create custom serializers by inheriting from `Serializer` or `ModelSerializer`. Here's an example:

```python
from your_application.serializers import ModelSerializer
from your_application.models import CustomModel

class CustomModelSerializer(ModelSerializer):
    class Meta:
        model = CustomModel
        fields = ['id', 'name', 'description']

# Usage
instance = CustomModel.query.get(1)
serializer = CustomModelSerializer(instance=instance)
print(serializer.data)
```