from django.urls import path
from app.views import *

urlpatterns = [

    path('', emp),  
    path('show', show),  
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', destroy), 
    
]