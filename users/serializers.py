from  django.contrib.auth.models import User
from rest_framework import serializers,validators

# class RegisterSerializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'email', 'first_name', 'last_name')

#         extra_kwargs = {
#             "password": {"write_only": True},
#             "email": {
#                 "required": True,
#                 "allow_blank": False,
#                 "validators": [
#                     validators.UniqueValidator(
#                         User.objects.all(), "A user with that email already exists."
#                         )
#                     ] 
#                 },
#         }
#     def create(self, validated_data):
#         usename = validated_data.get('username')
#         password = validated_data.get('password')
#         email = validated_data.get('email')
#         first_name = validated_data.get('first_name')
#         last_name = validated_data.get('last_name')
    
#         user = User.objects.create_user(
#             username=usename,
#             password=password,
#             email=email,
#             first_name=first_name,
#             last_name=last_name
#         )
#         return user
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
    )
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user