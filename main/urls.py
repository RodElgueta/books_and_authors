from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('second/<name>', views.second),
    path('create',views.createwiz),
    path('del',views.delwiz),
    path('createninja',views.createninja),
    path('dojos',views.ninjas)
]
