from django.urls import path
from . import views

urlpatterns = [
    path('', views.bug_list, name='bug_list'),
    path('report-bug/', views.bug_create, name='bug_create'),
    path('log/<uuid:bug_id>/', views.bug_detail, name='bug_detail'),
]
