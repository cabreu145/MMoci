from django.shortcuts import render, get_object_or_404, HttpResponse

from .models import Postimage, Postvideo, pdf
from photologue.models import Gallery, Photo, ImageModel
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView
)


# Base.

def home(request):
    posts = Postimage.objects.all().order_by('-date')[0:3]
    print(posts)
    return render(request, 'miltonblog/index.html', {'posts':posts})

def about(request):
    return render(request, 'miltonblog/about.html')

def privacy(request):
    return render(request, 'miltonblog/privacy.html')

def descargas(request):
    posts = pdf.objects.all().order_by('id')
    print(posts)
    return render(request, 'miltonblog/sonrisas.html', {'posts':posts})

# Posts Videos.
def video_view(request):
    posts = Postvideo.objects.all().order_by('id')
    print(posts)
    return render(request, 'miltonblog/videolist.html', {'posts':posts})

# Posts Images.
def blog_view(request):
    posts = Postimage.objects.all().order_by('id')
    print(posts)
    return render(request, 'miltonblog/postfotos.html', {'posts':posts})

def detail_view(request, id ):
    post = get_object_or_404(Postimage, id=id,)
    postinfo = Postimage.objects.filter(id=id)
    gallery = Gallery.objects.filter(extended=post)
    photo = Photo.objects.filter(extendeds=post).order_by('date_taken')
    
    
    return render(request, 'miltonblog/detallesfotos.html', {
        'post':post,
        'postinfo':postinfo,
        'gallery':gallery,
        'photo':photo,
         
        
        
    })


class Error404View(TemplateView):
    template_name = "miltonblog/error_404.html"


class Error505View(TemplateView):
    template_name = "miltonblog/error_500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view