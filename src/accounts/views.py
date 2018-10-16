from django.shortcuts import render
from contrib.views import View


class SignInUp(View):
    def get_template(self, request, *args, **kwargs):
        return render(request, 'accounts/signinup.html', {})

    def post(self, request, *args, **kwargs):
        pass
