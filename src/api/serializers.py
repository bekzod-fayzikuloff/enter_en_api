from typing import Optional, OrderedDict

from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "password", "password_confirm", "email")

    def validate(self, attrs: OrderedDict) -> Optional[OrderedDict]:
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(username=validated_data["username"], email=validated_data["email"])

        user.set_password(validated_data["password"])
        user.save()

        return user
