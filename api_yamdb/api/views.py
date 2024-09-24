from os.path import isabs
from pickle import FALSE
from random import random, randint

from django.core.mail import send_mail
from django.core.serializers import serialize
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from api.paginations import CustomPagination
from api.permissions import UserCreate, CategoryCreateOrReadOnly
from api.serializers import CreateUserSerializer, CreateTokenSerializer, CategorySerializer, UpdateUserSerializer, \
    GenreSerializer, TitleSerializer, ReviewSerializer
from reviews.models import CustomUser, Category, Genre, Review, Title


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class CreateUserViewSet(APIView):
    serializer_class = CreateUserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (UserCreate,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):

            confirmation_code = randint(000000, 999999)

            send_mail(
                'Your confirmation code',
                f'Your confirmation code is {confirmation_code}',
                'from@gmail.com',
                [serializer.validated_data['email']],
                fail_silently=False,
            )
            serializer.validated_data['confirmation_code'] = confirmation_code
            serializer.save()
            return Response('Good', status=status.HTTP_201_CREATED)

class UpdateUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['PATCH', 'GET'], url_path='me', permission_classes=(IsAuthenticated,))
    def get_me(self, request):
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        elif request.method == "PATCH":
            serializer = self.get_serializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetJWTTokenView(TokenObtainPairView):
    serializer_class = CreateTokenSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    pagination_class = CustomPagination
    permission_classes = (CategoryCreateOrReadOnly,)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    pagination_class = CustomPagination
    permission_classes = (CategoryCreateOrReadOnly,)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all().order_by('name')
    serializer_class = TitleSerializer
    pagination_class = CustomPagination
    permission_classes = (CategoryCreateOrReadOnly,)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('title')
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    permission_classes = (CategoryCreateOrReadOnly,)

    def get_queryset(self, request):
        post_pk = self.request.query_params.get('post_pk', None)


