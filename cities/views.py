from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.

from .models import City

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = "search_results.html"
    # queryset = City.objects.filter(name__icontains='Boston')

    def get_queryset(self):
        # return City.objects.filter(name__contains='Boston')
        # return City.objects.filter(
        #     Q(name__icontains='Boston') | Q(state__icontains='NY')
        # )
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )  
        return object_list