from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с User"""
    username = serializers.SlugField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='Пользователь с таким username уже'
                                            'существует')]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='Пользователь с таким email уже'
                                            'существует')]
    )
    password = serializers.CharField(max_length=128,
                                     write_only=True,
                                     validators=[validate_password],
                                     style={"input_type": "password"})
    class Meta:
        model = User
        fields = ('email',
                  'username',
                  'password')
