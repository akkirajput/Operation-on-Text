from django.urls import path
from . import views
urlpatterns=[
     path('',views.index,name='index'),
    path('process',views.process,name='process'),
    path('analyze',views.analyze,name='analyze')
    
   
]    
