from django.shortcuts import render
from django.views import View
from apps.user.tasks import create_user_token


class AuthIndex(View):
    template_name = 'auth/index.html'

    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            setattr(request.user, 'token', create_user_token(request.user).key)
        else:
            self.template_name = 'auth/login.html'
        return render(request, self.template_name, context)
