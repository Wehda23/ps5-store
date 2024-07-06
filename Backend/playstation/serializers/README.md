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

To handle nested relationships, you can define nested serializers and use them in your main serializer. Here's an example:

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

### Integration with Pydantic Models

You can also integrate Pydantic models for additional validation. Here's an example:

```python
from your_application.serializers import UserSerializer
from pydantic import BaseModel, EmailStr

class UserPydanticModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class UserPydanticSerializer(UserSerializer):
    pydantic_model = UserPydanticModel

    def validate_pydantic(self, data):
        try:
            self.pydantic_model(**data)
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
    print("Valid data")
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

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.