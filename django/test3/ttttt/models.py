from django.db import models

# Create your models here.
class TeParentModel(models.Model):
	comment = models.CharField(max_length=20)
	class Meta:
		db_table = 'tparent'

class TeChildModel(TeParentModel):
	name = models.CharField(max_length=20)
	class Meta:
		db_table = 'tchild'
