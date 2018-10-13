from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, ListView
from .models import DailyRecord

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
	template_name = 'contact.html'
	#queryset = DailyRecord.objects.all()
	test = 'test'
	context = {
		#"object_list": queryset
		"test":test

	}
	return render(request, template_name, context)

class DailyRecordListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get('slug')
		if slug:
			queryset = DailyRecord.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug) 

				)
		else:
			queryset = DailyRecord.objects.all()
		return queryset

