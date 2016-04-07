from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2

class Wstation(models.Model):
	station_name = models.CharField(max_length=200)
	def __str__(self):
		return unicode(self.station_name)

class Wproperty(models.Model):
	pass
	station = models.ForeignKey(Wstation, on_delete=models.CASCADE)
	rec_date = models.DateTimeField('date recorded')
	rec_temp = models.DecimalField(max_digits=6, decimal_places=3, null=True)
	rec_rh = models.DecimalField(max_digits=5, decimal_places=2, null=True)
	def __str__(self):
		return unicode(self.rec_date)
