from django.http import HttpResponse
from django.urls import path
from .views import BlogView


def Home(request):
    return HttpResponse(f"Login User: {request.user}")


urlpatterns = [
    path("", BlogView, name="Home"),
]
