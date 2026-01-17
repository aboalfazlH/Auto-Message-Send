from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("home-page")

def form_valid(self, form):
    response = super().form_valid(form)
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(self.request, username=username, password=password)
    if user is not None:
        login(self.request, user)
    return response