from django.urls import path
from apps.service.views import serviceView

urlpatterns = [
    path('service/', serviceView, name='service')
]