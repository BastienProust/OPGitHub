from django.http import HttpResponse
import requests
import webbrowser

def index(request):
    go()
    return HttpResponse("Welcome to a new page")
def go():
    url = 'https://console.ocp-311-intra-dev.mousquetaires.com:443/apis/build.openshift.io/v1/namespaces/dau-g0-dev/buildconfigs/python/webhooks/3f67832fcd8bbb02/generic'
    x = requests.post(url)
    webbrowser.open('https://google.com')
