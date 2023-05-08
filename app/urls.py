from django.urls import path
from .views import HomeView
from . import views

app_name='app'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('list/',views.list,name='list')
]
