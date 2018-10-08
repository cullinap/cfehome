from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html'

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		test = 'test'
		context = {
			"test": test

		}
		return context

class AboutView(View):
	def get(self, request, *args, **kwargs):
		context ={}
		return render(request, 'about.html', context)


def contact(request):
	context = {}
	return render(request, 'contact.html', context)

