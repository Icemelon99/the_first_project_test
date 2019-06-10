from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class FileTest(models.Model):
	file = models.FileField(upload_to='fileupload/')

class GoodInfo(models.Model):
	gcontent = HTMLField()
	
	class Meta:
		verbose_name = '富文本编辑器'
