from django.urls import path
from .views import bug_list, bug_create

urlpatterns = [
    path('', bug_list, name='bug_list'),
    path('create/', bug_create, name='bug_create'),
]
