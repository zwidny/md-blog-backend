from django.views.generic import View as DJView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class View(DJView):
    method = None

    def __init__(self, **kwargs):
        super(View, self).__init__(**kwargs)

    def get_http_method_names(self):
        if self.method is None:
            return self.http_method_names
        return self.http_method_names + [self.method, ]

    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        method = self.method or request.method.lower()

        if method in self.get_http_method_names():
            handler = getattr(self, method, self.http_method_not_allowed)
            if request.is_ajax():
                handler = getattr(self, "{}_ajax".format(method), handler)
            else:
                handler = getattr(self, "{}_template".format(method), handler)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class LoginView(View):
    pass


@method_decorator(csrf_exempt, name='dispatch')
class APIView(View):
    pass
