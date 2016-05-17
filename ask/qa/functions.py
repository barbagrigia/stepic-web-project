from django.core.paginator import Paginator, EmptyPage
from django.http import Http404

def pagepag(request, qs, url):
	try:
		limit = int(request.GET.get('limit', 10))
	except ValueError:
		limit = 10
	if limit > 100:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	paginator.baseurl = url
	return [paginator,page]
