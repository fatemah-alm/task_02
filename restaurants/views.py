from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def helloworld(request):
        return render(request, 'rest.html', {'msg':' Hello World!'})