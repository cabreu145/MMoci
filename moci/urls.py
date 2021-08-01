"""moci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls import *

from django.views.generic import CreateView
from photologue.models import Photo

from photologue.views import GalleryListView

from miltonblog import views

from django.conf.urls import handler404, handler500

from miltonblog.views import Error404View, Error505View

from django.conf.urls import url

from django.conf import settings

from django.views.static import serve





urlpatterns = [
    path('', include('miltonblog.urls')),
    #paths admin
    path('admin/', admin.site.urls),
    #path photologue
    path(r'foto/', include('photologue.urls', namespace='photologue')),
    
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    

]
handler404 = Error404View.as_view()

handler500 = Error505View.as_error_view()