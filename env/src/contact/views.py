from django.shortcuts import render
from .models import Info

# Create your views here.
def about(request):
	stuff = Info.objects.values('about')
	args = {
	'stuff': stuff,
	}
	return render(request,'about.html',args)