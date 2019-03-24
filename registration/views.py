# from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
# Para validar acceso
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = UserCreationFormWithEmail
    # No permite concatenar
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo de ejecucion 
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].label = ''
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        form.fields['username'].label = ''
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password1'].label = ''
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repita la contraseña'})
        form.fields['password2'].label = ''
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = 'registration/profile_form.html'

