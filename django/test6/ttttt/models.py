from django.db import models

# Create your models here.
class TestParentModel(models.Model):
	comment = models.CharField(max_length=20)
	class Meta:
		db_table = 'test_parent'

class TestChildModel(TestParentModel):
	name = models.CharField(max_length=20)
	class Meta:
		db_table = 'test_child'
