from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    phone = serializers.CharField(required=True, source='StudentProfile.phone')
    telegramId = serializers.CharField(required=False, source='StudentProfile.telegramId')
    isPaid = serializers.BooleanField(default=False, source='StudentProfile.isPaid')

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'phone', 'telegramId', 'isPaid')


class ProfileImageSerializer(serializers.Serializer):
    profileImage = serializers.ImageField(required=False, source='StudentProfile.profileImage')

    class Meta:
        model = User
        fields = ('profileImage', )

    def update(self, instance, validated_data):
        instance.profileImage = validated_data['profilePic']
        instance.save()
        return instance


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('password', )

    def update(self, instance, validated_data):
        instance.password = validated_data['password']
        instance.save()
        return instance