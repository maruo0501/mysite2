from django.urls import path
from .views import ListClass, DetailClass, FormClass, ConfirmClass, CreateClass, UpdateClass, DeleteClass

urlpatterns = [
    path('list/', ListClass.as_view(), name='list'),
    path('<int:pk>/', DetailClass.as_view(), name='detail'),
    path('form/', FormClass.as_view(), name='form'),
    path('confirm/', ConfirmClass.as_view(), name='confirm'),
    path('create/', CreateClass.as_view(), name='create'),
    path('<int:pk>/update/', UpdateClass.as_view(), name='update'),
    path('<int:pk>/delete/', DeleteClass.as_view(), name='delete'),
]