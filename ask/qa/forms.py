# coding: utf-8

from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class AskForm(forms.Form):
	author = forms.CharField(label='Ваше Имя', max_length=255)
	title = forms.CharField(label='Заголовок вопроса', max_length=255)
	text = forms.CharField(label='Текст вопроса', widget=forms.Textarea)
	
	def save(self):
		quest = Question(**self.cleaned_data)
		quest.save()
		return quest.pk

class AnswerForm(forms.Form):
	author = forms.CharField(label='Ваше Имя', max_length=255)
	text = forms.CharField(label='Текст ответа', widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def save(self):
		newanswer = Answer(text=self.cleaned_data['text'], author=self.cleaned_data['author'])
		newanswer.question = Question.objects.get(pk=self.cleaned_data['question'])
		newanswer.save()
		return self.cleaned_data['question']

class SignupForm(forms.Form):
	username = forms.CharField(label="Ваше имя", max_length=255)
	email = forms.EmailField(label="Ваша почта", widget=forms.EmailInput)
	password = forms.CharField(label="Ваш пароль", max_length=255, widget=forms.PasswordInput)
	def save(self):
		newuser = User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'],self.cleaned_data['password'])
		newuser.save()
		return newuser

class LoginForm(forms.Form):
	username = forms.CharField(label="Ваше имя", max_length=255)
	password = forms.CharField(label="Ваш пароль", max_length=255, widget=forms.PasswordInput)
	def input(self):
		user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
		if user is not None:
			if user.is_active:
				return user
		return None
