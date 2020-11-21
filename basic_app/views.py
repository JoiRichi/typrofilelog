from django.shortcuts import render
from basic_app.models import Profile
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, CreateView 


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