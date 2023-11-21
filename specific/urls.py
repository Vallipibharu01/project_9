from django.urls import path
from specific.views import *

app_name ='specific'

urlpatterns = [
    path('nag/',nag,name='nag'),
    path('gani/',gani,name='gani')
]
