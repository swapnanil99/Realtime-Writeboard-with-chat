from django.contrib import admin
from django.urls import path
from writeboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.whiteboard_view, name='whiteboard'),
]
