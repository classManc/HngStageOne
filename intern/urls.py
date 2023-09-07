from django.urls import path
from .views import InternDetails

urlpatterns = [
    path('api', InternDetails.as_view(), name='intern_details')
]
