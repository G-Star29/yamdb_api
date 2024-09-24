from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UpdateUserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'genres', views.GenreViewSet)
router.register(r'titles', views.TitleViewSet)
router.register(r'titles/(?P<post_pk>\d+)/reviews', views.ReviewViewSet)

urlpatterns = [
    path('v1/auth/signup/', views.CreateUserViewSet.as_view()),
    path('v1/auth/token/', views.GetJWTTokenView.as_view()),
    path('v1/', include(router.urls)),
]