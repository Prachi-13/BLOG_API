from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()  # returns active User Model in project


class UserPublicSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", lookup_field='pk')

    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", lookup_field='pk')
    days_since_joined = serializers.IntegerField(
        source='get_days_since_joined', read_only=True)
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'first_name', 'last_name', 'full_name',
            'email', 'days_since_joined',
            'is_active', 'date_joined', 'last_login'
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_superuser:
            representation['is_superuser'] = True
        else:
            representation['is_superuser'] = False
        if instance.is_staff:
            representation['is_staff'] = True
        else:
            representation['is_staff'] = False
        return representation


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password', 'password2',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', "")

        if not password or not password2:
            raise serializers.ValidationError(
                {'message': "Password field can't be empty"})
        if (password != password2):
            raise serializers.ValidationError(
                {'message': "Passwords don't match"})
        instance = self.Meta.model(**validated_data)
        if password == password2 and password is not None:
            instance.set_password(password)
        instance.save()

        return instance
