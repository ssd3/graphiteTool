from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView


def custom_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('graphql/')
    else:
        return LoginView.as_view()(request)
