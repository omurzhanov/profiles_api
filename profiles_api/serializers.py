from dataclasses import field
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile model"""
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }
    
    def create(self, validated_data):
        """Create a user"""
        email = validated_data.get('email')
        name = validated_data.get('name')
        password = validated_data.get('password')

        user = User.objects.create_user(email, name, password)

        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)
