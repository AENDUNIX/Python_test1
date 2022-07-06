from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from account.models import UserInfo


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            is_superuser=True,
            is_staff=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class InfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('user', 'name', 'user_name', 'user_telegram_id')

    def create(self, validated_data):
        info = UserInfo.objects.create(
            user=validated_data['user'],
            name=validated_data['name'],
            user_name=validated_data['user_name'],
            user_telegram_id=validated_data['user_telegram_id'],
        )
        info.save()
        return info
