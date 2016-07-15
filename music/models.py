from __future__ import unicode_literals

from django.db import models

class Artista(models.Model):
	nombre = models.CharField(max_length=50)
	foto = models.ImageField(upload_to='images/artistas_foto',blank=True,null=True)
	biografia = models.TextField(blank=True,null=True)
	orden = models.IntegerField(default=0)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nombre

