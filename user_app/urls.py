from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('all', ListOfVisitors.as_view(), name='all')
]
