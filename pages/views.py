# from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PageListView(ListView):
    model = Page
    #paginate_by = 100  # if pagination is desired

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context

class PageDetailView(DetailView):
    model = Page

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['now'] = timezone.now()
    #    return context
