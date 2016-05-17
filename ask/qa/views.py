from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from django.http import Http404, HttpResponseRedirect
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
#import logging

#logger = logging.getLogger(__name__)

def paginate(request, qs):
  try:
    limit = int(request.GET.get('limit',10))
  except ValueError:
    limit = 10
  
  if limit > 100:
    limit = 10
 
  try:
    page = int(request.GET.get('page',1))
  except ValueError:
    raise Http404

  paginator = Paginator(qs, limit)
  try:
    page = paginator.page(page)
  except EmptyPage:
    page = paginator.page(paginator.num_pages)  
  return page, paginator

def test(request, *args, **kwargs):
  return HttpResponse('OK')

def qa_list_all(request):
   qa = Question.objects.all()
   qa = qa.order_by('-added_at')
   page, paginator = paginate(request,qa)
   
   return render(request,'questions_list.html', {'user':request.user, 'questions': page.object_list, 'paginator': paginator, 'page':page, })

def qa_popular_all(request):
   qa = Question.objects.all()
   qa = qa.order_by('-rating')
   page, paginator = paginate(request,qa)
   
   return render(request,'questions_popular_list.html', {'user':request.user, 'questions': page.object_list, 'paginator': paginator, 'page':page, })

def question(request, id):
   question = get_object_or_404(Question, pk=id)
   answers = Answer.objects.filter(question = question)
   form = AnswerForm(initial={'question': str(id)})
 
   return render(request, 'question.html', { 'user':request.user, 'question':question, 'answers':answers, 'form': form, })

def ask_add(request):
   if request.method == 'POST': 
     form = AskForm(request.POST)
     if form.is_valid():
       form._user = request.user 
       post = form.save()
       #url = post.get_url()
       return HttpResponseRedirect(reverse('question', args=[post.id]))
   else:
      form = AskForm()
  
   return render(request, 'ask_add.html', { 'form': form, })

def answer_add(request):
   if request.method == 'POST': 
     form = AnswerForm(request.POST)
     if form.is_valid():
       form._user = request.user 
       post = form.save()
       #url = post.get_url()
       return HttpResponseRedirect(reverse('question', args=[post.question.id]))
   return HttpResponseRedirect('/')

def signup_add(request):
   #logger.debug(request)
   if request.method == 'POST': 
      #logger.debug('signup_add:' + request.method)
      form = SignupForm(request.POST)
      #logger.debug('signup_add POST:' + request.POST['username'] + ',pass=' + request.POST['password']+ ',email=' + request.POST['email'])
      if form.is_valid():
        #logger.debug('signup_add form.is_valid:')
        user = form.save()
        if user is not None:
          login(request,user)
          #logger.debug('signup_add login')
          return HttpResponseRedirect('/')

   form = SignupForm()
   return render(request, 'signup.html', {'form': form,})


def login_add(request):
   #logger.debug(request)
   if request.method == 'POST': 
     #logger.debug('login_add:' + request.method)
     form = LoginForm(request.POST)
     #logger.debug('login_add POST:' + request.POST['username'] + ',pass=' + request.POST['password'])
     if form.is_valid():
         #logger.debug('login_add form.is_valid:')
         user = form.save()
         if user is not None:
           logout(request)
           login(request,user)
           #logger.debug('login_add login')
           return HttpResponseRedirect('/')

   form = LoginForm()
   return render(request, 'login.html', {'form': form,})
