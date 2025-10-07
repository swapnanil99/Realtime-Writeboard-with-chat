from django.shortcuts import render
from django.http import HttpResponse  # import HttpResponse for health check

def whiteboard_view(request):
    return render(request, 'writeboard/index.html')

def health_check(request):
    return HttpResponse("OK")  # simple response for Render health check
