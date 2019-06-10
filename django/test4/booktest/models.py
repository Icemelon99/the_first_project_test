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

	def book_person(self):
		person_name = list()
		for person in self.heroinfo_set.all():
			person_name.append(person.hname)
		return person_name


	read_comment.admin_order_field = 'bcomment'
	read_comment.short_description = '方法'
	book_person.short_description = '包含人物'

class HeroInfo(models.Model):
	hname = models.CharField(max_length=20)
	hgender = models.BooleanField(default=False)
	hcomment = models.CharField(max_length=200)
	hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
	isDelete = models.BooleanField(default=False)

	def __str__(self):
		return self.hname

class Colors(models.Model):
	colors = models.CharField(max_length=20)
	def __str__(self):
		return self.colors

class Ball(models.Model):
	color = models.OneToOneField('Colors', on_delete=models.CASCADE)
	description = models.CharField(max_length=20)
	def __str__(self):
		return self.description

class Clothes(models.Model):
	color = models.ForeignKey('Colors', on_delete=models.CASCADE)
	description = models.CharField(max_length=20)
	def __str__(self):
		return self.description

class Child(models.Model):
	name = models.CharField(max_length=20)
	favor = models.ManyToManyField('Colors')
	def __str__(self):
		return self.name

# class Book(models.Model):
# 	name = models.CharField(max_length=20)
# 	manager = MyManager()

# class MyManager(models.Manager):
# 	def all(self):
# 		books = super().all().filter(isDelete=False)
# 		return books

# 	def createbook(self, name):
# 		book = self.model()
# 		book.name = name
# 		book.save()
# 		return book
class PicTest(models.Model):
	pic = models.ImageField(upload_to='booktest/')

	def __str__(self):
		return str(self.pic)


