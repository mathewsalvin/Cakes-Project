from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:

        model = Profile

        fields = ['username', 'password', 'first_name', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['email'] = validated_data['username']
        return Profile.objects.create_user(password=password, **validated_data)
