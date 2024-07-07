# Serializer Module for Flask Application

This module provides a set of serializers for your Flask application, allowing you to easily validate and serialize data. The serializers are built with flexibility and extendability in mind, providing features such as nested serialization and integration with Pydantic models.

## Installation

To use the serializers in your project, simply include the necessary files in your application directory.

## Usage

Can be used to Serialize SQLAlchemy Model or Flask-SQLAlchemy model.

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
from your_application.serializers import UserSerializer, SerializerError
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

## Serializer Validated Fields

You can customize your field validation by adding `validate_<field_name>` methods in your `serializers.Serializer class`.

Can be used in SQLAlchemy and Flask API

```py
from your_application import serializers
from your_application.models import CustomModel
from your_application.validators import CustomValidator
from typing import Union

class CustomPydantic(BaseModel):
    id: str
    name: str
    description: EmailStr

class CustomModelSerializer(serializers.Serializer):
    # If not specified the validate_pydantic method won't be called hence no errors will occure
    pydantic_model: BaseModel = CustomPydantic

    class Meta:
        model = CustomModel
        fields = ['id', 'name', 'description']

    # Custom Validation for name
    def validate_name(self, value):
        # This will trigger Custome made Validator or pass
        CustomValidator(SerializerError).validate(value)
        return value


def serialize(data: dict) -> Union[dict, list[dict]]:
    # To trigger validators you have to initiate .is_valid() method
    serializer = CustomModelSerializer(data=data)

    try:
        # Trigger validation
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        # If validation did not pass custom validation Grab Errors
        return serializer.errors
        # if validation did not pass Pydantic Validation
    except ValidationError as e: # If pydanic model not defined this error will not occure because validate_pydantic wont be called.
        return e.errors()
        # other unexpected or unhandled errors.
    except Exception as e:
        return e

serialize({'name': 'test', 'description': 'test@test.com',"id":1})
```

### Flask API Example

Here’s how you can integrate this serializer in a Flask API:

```py
from flask import Flask, request, make_response, Response
from your_application import serializers
from your_application.models import CustomModel
from your_application.validators import CustomValidator
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Union

# Define the Pydantic model
class CustomPydantic(BaseModel):
    id: str
    name: str
    description: EmailStr

# Define the serializer
class CustomModelSerializer(serializers.Serializer):
    pydantic_model: BaseModel = CustomPydantic

    class Meta:
        model = CustomModel
        fields = ['id', 'name', 'description']

    def validate_name(self, value):
        CustomValidator(SerializerError).validate(value)
        return value

# Flask app setup
app = Flask(__name__)

@app.route('/serialize', methods=['POST'])
def serialize_data(*args, **kwargs) -> Response:
    data = request.get_json()
    serializer = CustomModelSerializer(data=data)

    try:
        if serializer.is_valid():
            serializer.save()
            return make_response(serializer.data, 201)
        return make_response(serializer.errors, 400)
    except ValidationError as e:
        return make_response(e.errors(), 422)
    except Exception as e:
        return make_response({"error": str(e)}, 500)

if __name__ == '__main__':
    app.run(debug=True)

# Testing the endpoint with sample data
# You can use curl or Postman to test the endpoint
# curl -X POST http://127.0.0.1:5000/serialize -H "Content-Type: application/json" -d '{"id": "1", "name": "test", "description": "test@test.com"}'
```

### Explanation of the Flask API Example:

1. **Flask Imports:**
    - Imports necessary Flask components (`Flask`, `request`, `jsonify`).

2. **Serializer Setup:**
    - Defines `CustomPydantic` and `CustomModelSerializer` as before.

3. **Flask App Initialization:**
    - Sets up a basic Flask application.
    - Defines an endpoint `/serialize` that accepts POST requests with JSON data.

4. **Endpoint Logic:**
    - Initializes the `CustomModelSerializer` with the incoming data.
    - Checks if the data is valid using `serializer.is_valid()`.
    - Saves and returns the serialized data if valid.
    - Returns validation errors if any occur.
    - Handles Pydantic validation errors and other exceptions.

5. **Running the App:**
    - Runs the Flask app in debug mode.

### Testing the Endpoint:
You can test the endpoint using tools like `curl` or Postman by sending a POST request with the appropriate JSON data to `http://127.0.0.1:5000/serialize`.

This example shows how to integrate the custom Pydantic serializer with Flask, including custom validation and error handling, while keeping the original structure and logic of the provided code.
