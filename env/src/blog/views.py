from django.shortcuts import render,Http404
from django.core.paginator import Paginator 
from .models import Post

# Create your views here.
def index(request):
	blog = Post.objects.all()
	paginator = Paginator(blog,5)
	page = request.GET.get('page')
	blog = paginator.get_page(page)
	args = {
	'blog':blog
	}
	return render(request,'blogindex.html',args)

def blogdetail(request,slug):
	try:
		objects = Post.objects.all()
		blog = Post.objects.get(slug=slug)
		context = {'blog':blog,
		'objects':objects,
		}
		return render(request,'blogdetail.html',context)
	except:
		raise Http404