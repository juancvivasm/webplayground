from django.urls import path
#from . import views
from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], 'profiles')
