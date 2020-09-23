from django.http import HttpResponse
from pythonping import ping


def index(request):
    return HttpResponse(ping('8.8.8.8'))
