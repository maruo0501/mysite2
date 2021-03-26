from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from polls.models import Question
from .serializers import QuestionSerializer

class QuestionListAPIView(ListAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class QuestionCreateAPIView(CreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class QuestionDestroyAPIView(DestroyAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class QuestionUpdateAPIView(UpdateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer

class QuestionRetrieveAPIView(RetrieveAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
