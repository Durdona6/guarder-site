from django.urls import path
from apps.about.views import aboutView

urlpatterns = [
    path('about/', aboutView, name='about')
]