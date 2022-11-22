from django.views.generic.base import TemplateView
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Home View.")
class HomeView(TemplateView):
    template_name = "mysite/home.html"
    