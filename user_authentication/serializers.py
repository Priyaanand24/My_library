from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},  # make the password write-only
            'date_joined': {'read_only': True},  # Automatically set by django
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # creates a user with hased password
        return user

"""User.objects.create_user(**validated_data) creates a new user using the validated
 data and securely hashes the password before storing it in a db."""

"""The **validated_data unpacks the dictionary of validated fields and passes them as 
keyword arguments to the create_user method."""