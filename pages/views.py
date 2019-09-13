from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
		template_name = 'index.html'

class ManEaterView(TemplateView):
		template_name = 'maneater.html'

class OrchidView(TemplateView):
		template_name = 'orchid.html'

class BlueView(TemplateView):
		template_name = 'blue.html'

# Create your views here.
