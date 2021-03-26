from django.urls import path

from .views import QuestionListAPIView, QuestionCreateAPIView, QuestionDestroyAPIView, QuestionUpdateAPIView, QuestionRetrieveAPIView

urlpatterns = [
    path('list/', QuestionListAPIView.as_view()),
    path('create/', QuestionCreateAPIView.as_view()),
    path('destroy/<int:pk>/', QuestionDestroyAPIView.as_view()),
    path('update/<int:pk>/', QuestionUpdateAPIView.as_view()),
    path('list/<int:pk>/', QuestionRetrieveAPIView.as_view()),

]