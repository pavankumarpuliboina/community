from django.db import models
from authentication.models import MyUser
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
	category = models.CharField(max_length = 200)
	slug = models.SlugField()

	def __str__(self):
		return self.category

	def recent(self):
		return self.category.question_set.all()

	class Meta:
		verbose_name_plural = 'Category'


class Question(models.Model):
	user = models.ForeignKey(MyUser, on_delete = models.CASCADE)
	question = models.CharField(max_length = 500, blank = True)
	description  = models.TextField(max_length = 5000, blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now = True, blank = True, null = True)
	userlabel = models.CharField(max_length = 50, default="Newcommer") # Begginer Expert Newcomer
	answerlabel = models.CharField(max_length=50,blank = True) #Best Answer
	upvote = models.IntegerField(default="0")
	downvote = models.IntegerField(default="0")
	slug = models.SlugField(blank=True,null=True)

	def __str__(self):
		return self.question


class Answer(models.Model):
	answer = RichTextField(blank = True, null = True)
	question = models.ForeignKey(Question, on_delete = models.CASCADE)
	answeredby = models.ForeignKey(MyUser, on_delete = models.CASCADE, blank = True, null = True)
	# slug = models.SlugField(blank=True,null=True)


	def __str__(self):
		return str(self.question)




