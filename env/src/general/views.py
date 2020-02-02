from django.shortcuts import render
from .models import General

# Create your views here.
def info(request):
	gens = General.objects.values('contact','email')
	args = {'gens':gens,
	}
	return render(request,'contact.html',args)

def about(request):
	gens = General.objects.values('about')
	args = {'gens':gens,
	}
	return render(request,'about.html',args)