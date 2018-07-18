from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import LoginForm
from allauth.account.views import SignupView

import json

class LoginView(TemplateView):
    """ Login View
    """
    template_name = 'account/login.html'

    def get(self,*args,**kwargs):
        return  render(self.request,self.template_name,{})

    def post(self,*args,**kwargs):
        form = LoginForm(self.request.POST)
        
        if form.is_valid():
            login(self.request, form.user)

            if self.request.POST.get('remember_me'):
                self.request.session.set_expiry(31557600)
            else:
                self.request.session.set_expiry(0)

            return HttpResponse(status=200)

        errors = {}
        for error in form.errors:
            err = form.errors[error].as_text()
            errors[error] = str(err)

        errors['failed'] = form.errors['__all__'].as_text()

        return HttpResponseBadRequest(json.dumps(errors))

class LogoutView(LoginRequiredMixin, View):
    """ Logout View
    """
    def get(self, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse('main:index'))

class  ProfileView(TemplateView):
    """ Profile View
    """
    template_name = 'account/profile.html'
    def get(self, *args, **kwargs):
        return render(self.request,self.template_name,{})


