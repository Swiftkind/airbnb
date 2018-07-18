from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.conf import settings

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from accounts.forms import UserRegistrationForm

import json

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get(self,*args,**kwargs):
        form = UserRegistrationForm(self.request.GET or None)
        return render(self.request,self.template_name,{'form':form})

    def post(self,*args,**kwargs):
        form = UserRegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(self.request, user)
            return HttpResponse(status=201)

        errors = {}
        for error in form.errors:
            err = form.errors[error].as_text()
            errors[error] = str(err)
        return HttpResponseBadRequest(json.dumps(errors))
