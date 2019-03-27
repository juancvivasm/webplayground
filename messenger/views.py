from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name="dispatch")
class ThreadList(ListView):
    model = Thread

    # Se sobreescribe el metodo para devolver el hilo del usuario autenticado
    def get_queryset(self):
        queryset = super(ThreadList, self).get_queryset()
        return queryset.filter(users=self.request.user)

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
