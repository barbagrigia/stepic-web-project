from django import forms
from qa.models import Question, Answer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
  title = forms.CharField(max_length=255)
  text =  forms.CharField(widget=forms.Textarea)
  
  def clean_title(self):
    title = self.cleaned_data['title']
    if title.strip()=='':
      raise forms.ValidationError(u'Title is empty', code = 12)
    return title
    
  def clean_text(self):
    text = self.cleaned_data['text']
    if text.strip()=='':
      raise forms.ValidationError(u'Text is empty', code = 12)
    return text
      
  def save(self):
    if self._user.is_anonymous():
      self.cleaned_data['author_id'] = 1
    else:     
      self.cleaned_data['author'] = self._user
    post = Question(**self.cleaned_data)
    post.save()
    return post
   
   
class AnswerForm(forms.Form):
  text =  forms.CharField(widget=forms.Textarea)
  question = forms.IntegerField(widget=forms.HiddenInput)
  
  def clean_question(self):
    question = self.cleaned_data['question']
    if question == 0:
      raise forms.ValidationError(u'Answer need question', code = 12)
    return question
    
  def clean_text(self):
    text = self.cleaned_data['text']
    if text.strip()=='':
      raise forms.ValidationError(u'Text is empty', code = 12)
    return text

  def save(self):
#    self.cleaned_data['question'] = Question.objects.filter(pk = self.cleaned_data['question'])
    self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
  
    if self._user.is_anonymous():
      self.cleaned_data['author_id'] = 1
    else:     
      self.cleaned_data['author'] = self._user
    post = Answer(**self.cleaned_data)
    post.save()
    return post

class SignupForm(forms.Form):
   username = forms.CharField(max_length=255)
   email = forms.EmailField()
   password = forms.CharField(widget=forms.PasswordInput)
   
   def clean_username(self):
     text = self.cleaned_data['username']
     if text.strip()=='':
       raise forms.ValidationError(u'User name is empty', code = 12)
     return text
    
   def clean_password(self):
     text = self.cleaned_data['password']
     if text.strip()=='':
       raise forms.ValidationError(u'Password is empty', code = 12)
     return text

   def clean_email(self):
     text = self.cleaned_data['email']
     if text.strip()=='':
       raise forms.ValidationError(u'Email is empty', code = 12)
     return text

   def save(self):
     user = User.objects.create_user(**self.cleaned_data)
     user.save()
     auth = authenticate(**self.cleaned_data)
     return auth
    

class LoginForm(forms.Form):
   username = forms.CharField(max_length=255)
   password = forms.CharField(widget=forms.PasswordInput) 

   def clean_username(self):
     text = self.cleaned_data['username']
     if text.strip()=='':
       raise forms.ValidationError(u'User name is empty', code = 12)
     return text
    
   def clean_password(self):
     text = self.cleaned_data['password']
     if text.strip()=='':
       raise forms.ValidationError(u'Password is empty', code = 12)
     return text

   def save(self):
     user = authenticate(**self.cleaned_data)
     return user
