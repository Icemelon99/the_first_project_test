from django.db import models

# Create your models here.
class BookInfo(models.Model):
	btitle = models.CharField(verbose_name='书名', max_length=20)
	bpub_date = models.DateField()
	bread = models.IntegerField(default=0)
	bcomment = models.IntegerField(default=0)
	isDelete = models.BooleanField(default=False)

	def __str__(self):
		return self.btitle

	def read_comment(self):
		return str(self.bread)+'+'+str(self.bcomment)

	read_comment.admin_order_field = 'bcomment'
	read_comment.short_description = '方法'




class HeroInfo(models.Model):
	hname = models.CharField(max_length=20)
	hgender = models.BooleanField(default=False)
	hcomment = models.CharField(max_length=200)
	hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
	isDelete = models.BooleanField(default=False)

	def __str__(self):
		return self.hname