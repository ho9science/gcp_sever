from django.db import models

# Create your models here.
class Kknouns(models.Model):
	class Meta:
		db_table='kknouns'
	id=models.IntegerField(primary_key=True, max_length=11)
	indexing=models.CharField(max_length=200)
	answer=models.CharField(max_length=767)

class mecabnouns(models.Model):
	class Meta:
		db_table='mecabnouns'
	idx=models.IntegerField(primary_key=True, max_length=11)
	indexing=models.CharField(max_length=255)
	answer=models.CharField(max_length=767)