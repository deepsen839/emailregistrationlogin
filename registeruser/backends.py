#from django.contrib.auth.models import User
from django.conf import settings
from .models import myUser
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

class EmailAuthBackend(ModelBackend):

    """Allow users to log in with their email address"""

    def authenticate(self, email=None, password=None, **kwargs):
        # Some authenticators expect to authenticate by 'username'
        if email is None:
            email = kwargs.get('username')

        try:
            user = myUser.objects.all(email)
            if user.check_password(password):
                user.backend = "%s.%s" % (self.__module__, self.__class__.__name__)
                return user
        except myUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return myUser.objects.get(pk=user_id)
        except myUser.DoesNotExist:
            return None