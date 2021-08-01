from django.urls import include, path
from django.conf.urls import *
from django.views.generic import CreateView
from photologue.models import Photo
from django.conf.urls import handler404



from photologue.views import GalleryListView
from . import views 
urlpatterns = [
    #paths index
    path('', views.home, name='home'),
    path('Acerca', views.about, name='about'),
    path('Politica-de-privacidad', views.privacy, name='privacy'),
    #path post
    path('Fotos/', views.blog_view, name='fotos'),
    path('Fotos/<int:id>/', views.detail_view, name='detallesfotos'),
    #path videos
    path('Videos/', views.video_view, name='video'),
    path('Descarga/', views.descargas, name='sonrisas'),
     
    
]
