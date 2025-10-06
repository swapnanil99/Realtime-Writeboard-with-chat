from django.shortcuts import render

def whiteboard_view(request):
    return render(request, 'writeboard/index.html')