from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
# TODO: регистрация
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from account.forms import ChangePasswordForm, RegistrationForm


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('movie_list')
    print()


# TODO: логин
class SigninView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('movie_list')


# TODO: смена пароля
class PasswordChangeView(LoginRequiredMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'
    success_url = reverse_lazy('change-password-done')
    login_url = reverse_lazy('signin')

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs()
        print(kwargs)
        kwargs['user'] = self.request.user
        print(kwargs)
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



class PasswordChangeDoneView(TemplateView):
    template_name = 'account/change_password_done.html'

# TODO: логаут
# TODO: сверстать страницы BootStrap
# TODO: залить на север
