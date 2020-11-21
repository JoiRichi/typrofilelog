from django.shortcuts import render
from basic_app.models import Name, Profile
from django.views.generic import TemplateView, ListView, DetailView 


# Create your views here.
class IndexView(TemplateView):
	template_name = 'basic_app/index.html'


class NameListView(ListView):
	model = Name

class ProfileDetail(DetailView):
	model = Name