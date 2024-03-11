from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор пользователя'''

    class Meta:
        model = User
        fields = ('id', 'username', 'telegram_id', 'first_name', 'last_name', 'is_active',)


class UserCreateSerializer(serializers.Serializer):
    '''Сериализатор создания пользователя'''

    email = serializers.EmailField(max_length=80, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)

    def save(self, **kwargs):
        user = User(
            username=self.validated_data['email'],
            is_active=False
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()

    class Meta:
        model = User
        fields = ('username', 'password')