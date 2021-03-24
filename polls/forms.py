from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("question_text", "anser_text")
        labels={
            'question_text':'質問',
            'anser_text':'回答',
        }