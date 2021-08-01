from django.db import models
from django.db.models import Model

from photologue.models import Gallery, Photo
# imagenes, id, fecha, hora,  titulo, descripcion, categoria, estado, imagen portada, fotos photologue.

class Categoria(models.Model):
    cat = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = u'Categoria'
        verbose_name_plural = u'Categorias'

    def __str__(self):
        return self.cat


class Postvideo(models.Model):
    mp4 = models.TextField(verbose_name="Video mp4",  null=True, blank="True")
    webm = models.TextField(verbose_name="Video webm",  null=True, blank="True")
    title = models.CharField(max_length=250,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True,verbose_name="Creado")
    updated_on = models.DateField(auto_now=True, verbose_name="Actualizado")
    class Meta:
        verbose_name = u'Publicacion de video'
        verbose_name_plural = u'Publicaciones de videos'

    def __str__(self):
        return self.title

class Postimage(models.Model):
    photo = models.ManyToManyField(Photo, related_name='extendeds', blank=True,verbose_name="Fotos")
    gallery = models.ForeignKey(Gallery,related_name='extended', null=True, blank=True, on_delete=models.CASCADE,verbose_name="Galeria")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250,verbose_name="Titulo", blank=True)
    description = models.TextField(verbose_name="Descripcion", blank=True)
    image = models.FileField(upload_to = 'images/',blank=True,verbose_name="Foto Portada")
    date = models.DateTimeField(null=False, blank=False,verbose_name="Fecha")
    place =models.TextField(verbose_name="Lugar")
    created_on = models.DateField(auto_now_add=True,verbose_name="Creado")
    updated_on = models.DateField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = u'Publicacion'
        verbose_name_plural = u'Publicaciones'

    def __str__(self):
        return self.gallery
    def __str__(self):
        return self.title

class pdf(models.Model):
    pdf = models.FileField(upload_to = 'images/pdf',blank=False,verbose_name="sonrisas")

    class Meta:
        verbose_name = u'Pdf'
        verbose_name_plural = u'Pdfs'
