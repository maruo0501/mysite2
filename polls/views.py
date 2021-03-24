from django.shortcuts import render
# Create your views here.
from .models import Question
from django.views.generic import ListView, FormView, DetailView, DeleteView, UpdateView, CreateView
from.forms import QuestionForm
from django.urls import reverse_lazy

class ListClass(ListView):
    model = Question
    template_name = 'list.html'

class DetailClass(DetailView):
    model = Question
    template_name = 'detail.html'

class FormClass(FormView):
    form_class = QuestionForm
    template_name = 'form.html'
    def form_valid(self, form):
        return render(self.request, 'form.html', {'form': form})  
    
class ConfirmClass(FormView):
    form_class = QuestionForm
    template_name = 'confirm.html'
    def form_valid(self, form):
        return render(self.request, 'confirm.html', {'form': form})
    def form_invalid(self, form):
        return render(self.request, 'form.html', {'form': form})

class CreateClass(CreateView):
    form_class = QuestionForm
    success_url = reverse_lazy('list')
    def form_invalid(self, form):
        return render(self.request, 'form.html', {'form': form})

class UpdateClass(UpdateView):
    model = Question
    template_name = 'update.html'
    form_class = QuestionForm
    success_url = reverse_lazy('list')

class DeleteClass(DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = reverse_lazy('list')

