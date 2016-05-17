# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from models import Question, Answer
from functions import pagepag
from forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout


def test(request, *args, **kwargs):
  return HttpResponse('OK')


def basetemp(request, url, order='-added_ad'):
  questions = Question.objects.all()
  questions = questions.order_by(order)
  [paginator, page] = pagepag(request, questions, url)
  return render(request, 'index.html', {
    'questions': page.object_list,
    'paginator': paginator,
    'page': page,
    'user': request.user,
  }, )


def questpage(request, slug):
  question = get_object_or_404(Question, pk=slug)
  return render(request, 'quest.html', {
    'question': question,
    'answers': Answer.objects.filter(question=slug).order_by('-added_ad')[:],
    'newanswer': AnswerForm({'question': int(slug), 'author': request.user}),
  }, )


def askform(request):
  url = '/question/'
  if request.method == "POST":
    if request.POST.get('author'):
      author = request.POST.get('author')
    else:
      author = request.user
    ask = AskForm({
      'title': request.POST['title'],
      'text': request.POST['text'],
      'author': author,
    }, )
    if ask.is_valid():
      url = url + str(ask.save()) + '/'
    return HttpResponseRedirect(url)
  ask = AskForm({'author': request.user})
  return render(request, 'ask.html', {
    'ask': ask,
  }, )


def newanswer(request):
  url = '/question/'
  if request.method == "POST":
    newanswer = AnswerForm(request.POST)
    if newanswer.is_valid():
      url = url + str(newanswer.save()) + '/'
  return HttpResponseRedirect(url)


def signupform(request):
  if request.method == "POST":
    signup = SignupForm(request.POST)
    if signup.is_valid():
      signup = signup.save()
      loguser = LoginForm(request.POST)
      if loguser.is_valid():
        loguser = loguser.input()
        if loguser is not None:
          login(request, loguser)
      else:
        return HttpResponse('Invalid Data')
      return HttpResponseRedirect('/')
  return render(request, 'signup.html', {
    'signup': SignupForm(),
    'header': 'Зарегистрируйтесь',
    'url': 'signup'
  }, )


def loginform(request):
  if request.method == 'POST':
    loguser = LoginForm(request.POST)
    if loguser.is_valid():
      loguser = loguser.input()
      if loguser is not None:
        login(request, loguser)
      else:
        return HttpResponse('Not wright login or password')
      return HttpResponseRedirect('/')
    else:
      return HttpResponse('Invalid Data')
  return render(request, 'signup.html', {
    'signup': LoginForm(),
    'header': 'Войдите на сайт',
    'url': 'login',
  }, )


def logoutPage(request):
  logout(request)
  return HttpResponseRedirect('/')
