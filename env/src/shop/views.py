from django.shortcuts import render,Http404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 


from blog.models import Post
from .models import ShopInfo
from emails.forms import EmailSignUpForm
import json


def index(request):
	#EVERYTHING THAT IS IN THE HOMEPAGE
	form = EmailSignUpForm()
	shops = ShopInfo.objects.filter(status=1).order_by('-status')[0:2]
	blog = Post.objects.filter(status=1).order_by('-pub_date')[0:3]
	data = ShopInfo.objects.values('shop_name','slug', 'lat', 'lon','about')
	json_data = json.dumps(list(data))
	args = {'shops':shops,
	'blog':blog,
	'data':json_data,
	'form': form,
	}

	return render(request,'index.html',args)

def shopindex(request):
	#shop index with paginator effect
	shops = ShopInfo.objects.all()
	paginator = Paginator(shops,5)
	page = request.GET.get('page')
	# ?page=2 
	shops = paginator.get_page(page)

	arg = {'shops':shops,
	}
	return render(request, 'shopindex.html', arg)



def shopdetail(request,slug):
	#detailed view of shop
	try:
		shop = ShopInfo.objects.get(slug=slug)
		context = {'shop':shop
		}
		return render(request,'shopdetail.html',context)
	except:
		raise Http404

