from django.urls import path
from . import views

urlpatterns=[
path('run/',views.run),
path('ran/',views.ran),
path('box/',views.box)

]