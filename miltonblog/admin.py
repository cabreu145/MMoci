from django.contrib import admin

from .models import Categoria, Postimage, Postvideo, pdf

admin.site.register(Categoria)
admin.site.register(Postimage)
admin.site.register(Postvideo)
admin.site.register(pdf)