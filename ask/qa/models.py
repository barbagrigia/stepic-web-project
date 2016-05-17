from django.db import models

#User model
from django.contrib.auth.models import User

#Question model
#title - заголовок вопроса
#text - полный текст вопроса
#added_at - дата добавления вопроса
#rating - рейтинг вопроса (число)
#author - автор вопроса
#likes - список пользователей, поставивших "лайк"

class Question(models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now = True)
	rating = models.IntegerField(default = 0)
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)

#Answer model
#text - текст ответа
#added_at - дата добавления ответа
#question - вопрос, к которому относится ответ
#author - автор ответа

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now = True)
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
