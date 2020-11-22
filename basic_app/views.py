from django.shortcuts import render
from basic_app.models import Profile
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView, DeleteView 


# Create your views here.
class IndexView(TemplateView):
	template_name = 'basic_app/index.html'


class NameListView(ListView):
	model = Profile

class ProfileDetail(DetailView):
	model = Profile

class ProfileCreateView(CreateView):
	template_name = 'basic_app/name_form.html'
	model = Profile
	fields = '__all__'

class profileUpdateView(UpdateView):
	template_name = 'basic_app/name_form.html'
	model = Profile
	fields = '__all__'

class ProfileDeleteView(DeleteView):
	model = Profile
	context_object_name = 'profile_delete'
	success_url = reverse_lazy('basic_app:list')