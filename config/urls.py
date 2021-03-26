"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]

# 追加
# from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
# class UdemyUserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')

# class UdemyUserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UdemyUserSerializer

# router = routers.DefaultRouter()
# router.register(r'users', UdemyUserViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

