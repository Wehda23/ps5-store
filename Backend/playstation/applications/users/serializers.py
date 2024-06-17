"""
# File the contains Serializers for User Application
"""
from playstation import serializers
from playstation.models.users import User


# User Registeration serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model: object = User
        fields: list[str] = [
            "first_name",
            "email",
            "last_name",
            "password"
        ]