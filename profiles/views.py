from django.shortcuts import render, get_list_or_404, get_object_or_404
from registration.models import Profile
# from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# def profiles(request):
#    profiles = get_list_or_404(Profile)
#    return render(request, 'profiles/profile_list.html', {'profiles':profiles})
class ProfileListView(ListView):
    model = Profile
    paginate_by = 3
    template_name = 'profiles/profile_list.html'

# def profile(request, username):
#    profile = get_object_or_404(Profile, user__username = username)
#    return render(request, 'profiles/profile_detail.html', {'profile':profile})
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
