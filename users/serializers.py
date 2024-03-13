from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор пользователя'''

    class Meta:
        model = User
        fields = ('id', 'username', 'telegram', 'first_name', 'last_name', 'is_active',)


class UserCreateSerializer(serializers.Serializer):
    '''Сериализатор создания пользователя'''

    username = serializers.CharField(max_length=200, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['username'],
            is_active=False
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return message(user)

    class Meta:
        model = User
        fields = ('username', 'password')