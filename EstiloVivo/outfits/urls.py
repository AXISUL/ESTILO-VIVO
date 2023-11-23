from django.urls import path
from . import views
from .views import outfits

urlpatterns = [
    path('outfits/', outfits, name='outfits'),
    path('', views.index),
    path('comofunciona/', views.comofunciona),
    path('comunidad/', views.comunidad),
    path('cameron/', views.cameron),
    path('resultados/', views.resultados_view, name='resultados'),
    path('prendaindividual/<int:outfit_id>/', views.prendaindividual_view, name='prendaindividual'),
    path('prendasEscogidas/', views.prendasEscogidas, name='prendasEscogidas'),
    
   
]
