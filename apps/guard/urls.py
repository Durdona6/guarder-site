from django.urls import path
from apps.guard.views import guarView

urlpatterns = [
    path('guard/', guarView, name='guar')
]