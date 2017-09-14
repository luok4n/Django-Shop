from django.db import models



class Marca(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.nombre)


class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	precio = models.IntegerField()
	cantidad = models.IntegerField()
	color = models.CharField(max_length=50)
	marca = models.ForeignKey(Marca, blank=True)
