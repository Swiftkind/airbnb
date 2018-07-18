from django.apps import AppConfig

from allauth.account.signals import user_signed_up, user_logged_in

from .signals import *


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        user_signed_up.connect(on_user_signed_up)
        user_logged_in.connect(on_user_logged_in)
