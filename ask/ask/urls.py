from django.conf.urls import url
from django.contrib import admin
from qa.views import test, basetemp, questpage, askform, newanswer, signupform, loginform, logoutPage

urlpatterns = [
	url(r'^$', basetemp, {'url':'/?page=','order':'-added_ad'}),
	url(r'^login/.*$', loginform),
	url(r'^logout/.*$', logoutPage),
	url(r'^signup/.*$', signupform),
	url(r'^question/(?P<slug>\d+)/$', questpage),
	url(r'^question/$', askform),
	url(r'^ask/.*$', askform),
	url(r'^popular/.*$', basetemp, {'url':'/popular/?page=','order':'-likes'}),
	url(r'^new/.*$', test),
	url(r'^answer/.*$', newanswer),
]
