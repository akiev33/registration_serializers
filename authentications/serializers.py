from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate, password_validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

USER_TYPE_CHOICES = (
    ('user', 'User'),
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, required=True, write_only=True)
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0][0])

    class Meta:
        model = User
        fields = [
            'email', 'user_type',  'password', 'password_confirmation'
        ]

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists:
            raise serializers.ValidationError('user with given email  exist')
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError("doesn't much")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('user email not found')
        return value

    def validate(self, attrs):
        email = attrs.get('email')

        password = attrs.pop('password', None)

        if not User.objects.filter(email=email,).exists():
            raise serializers.ValidationError("not found")
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True, min_length=6)
    new_password1 = serializers.CharField(required=True, write_only=True, min_length=6)
    new_password2 = serializers.CharField(required=True, write_only=True, min_length=6)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Your old password was entered incorrectly. Please enter it again.')
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': "The two password fields didn't match."})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


