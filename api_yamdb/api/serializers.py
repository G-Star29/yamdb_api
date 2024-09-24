from email.policy import default

from django.db.models import Sum, Avg
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import CustomUser, Category, Genre, Review, Title


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'bio', 'role']
        read_only_fields = ['confirmation_code', 'role']
        def validate_username(self, value):
            if value.lower() == 'me':
                raise serializers.ValidationError('Username "me" is not vaild')
            return value

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'bio']
        read_only_fields = ['confirmation_code', 'role']


class CreateTokenSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.USERNAME_FIELD

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['confirmation_code'] = serializers.CharField(write_only=True)
        self.fields.pop('password')

    def validate(self, attrs):
        username = attrs.get(self.username_field)
        confirmation_code = attrs.get('confirmation_code')

        try:
            # Предполагаем, что confirmation_code хранится как целое число
            user = CustomUser.objects.get(**{self.username_field: username})
            if int(confirmation_code) != user.confirmation_code:
                raise serializers.ValidationError('Неверный код подтверждения')
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Пользователь не найден')

        # Генерируем токен без проверки пароля
        token = self.get_token(user)

        return {
            'refresh': str(token),
            'access': str(token.access_token)
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        read_only_fields = ['id']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'slug']
        read_only_fields = ['id']

class TitleSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ['id', 'rating']

    def get_rating(self, obj):
        score = Review.objects.filter(title=obj).aggregate(avg=Avg('score', default=0))
        return score['avg']

class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    title = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['id', 'author', 'pub_date', 'title']