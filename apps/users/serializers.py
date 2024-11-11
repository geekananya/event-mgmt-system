from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('first_name', 'last_name', 'email', 'is_admin')


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'is_admin')