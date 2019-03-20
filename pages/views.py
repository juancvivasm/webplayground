# from django.shortcuts import render, get_object_or_404, get_list_or_404
# from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
# from django.urls import reverse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    '''
    Es un mixin que exige que el usuario sea miembro del staff
    '''
    # Para controlar quien ingresa a esta vista
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # print(request.user)
        #if not request.user.is_staff:
        #    return redirect(reverse_lazy('admin:login'))

        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

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

class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']

    success_url = reverse_lazy('pages:pages')
    #def get_success_url(self):
    #    return reverse('pages:pages')

    # Para controlar quien ingresa a esta vista
    #def dispatch(self, request, *args, **kwargs):
    #    # print(request.user)
    #    if not request.user.is_staff:
    #        return redirect(reverse_lazy('admin:login'))

    #    return super(PageCreate, self).dispatch(request, *args, **kwargs)

class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    # fields = ['title', 'content', 'order']
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
