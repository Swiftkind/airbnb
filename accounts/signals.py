from django.http import HttpResponseRedirect

def on_user_signed_up(request,user, **kwargs):
    user.is_active = True
    user.save()

def on_user_logged_in(request,user, **kwargs):
    print('user loged in')