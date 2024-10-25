# training/views.py
from django.shortcuts import render, redirect
from django.views import View
from .models import Training
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class TrainingListView(ListView):
    model = Training
    template_name = 'training/training_list.html'

class TrainingCreateView(CreateView):
    model = Training
    template_name = 'training/training_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('training_list')

class TrainingDetailView(View):
    def get(self, request, pk):
        training = Training.objects.get(pk=pk)
        return render(request, 'training/training_detail.html', {'training': training})

class TrainingUpdateView(UpdateView):
    model = Training
    template_name = 'training/training_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('training_list')

class TrainingDeleteView(DeleteView):
    model = Training
    template_name = 'training/training_confirm_delete.html'
    success_url = reverse_lazy('training_list')
