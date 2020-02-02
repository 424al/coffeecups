from django.shortcuts import render
from django.contrib import messages
import requests
from django.conf import settings
from django.http import HttpResponseRedirect
import json
from .forms import EmailSignUpForm
from .models import Signup
from emails.forms import EmailSignUpForm
import mailchimp 


#MAILCHIMP KEYS
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://us4.api.mailchimp.com/3.0/'
members_endpoint = 'https://us4.api.mailchimp.com/3.0/lists/0db862cc64/members'

def subscribe(email):
	data = {
		"email_address": email,
		"status": "subscribed"
	}

	r = requests.post(
		members_endpoint,
		auth=('', MAILCHIMP_API_KEY),
		data = json.dumps(data)
		)
	return r.status_code, r.json()

def email_list_signup(request):
	#CHECKS IF FORM IS VALID. IF VALID, IT GOES TO MAILCHIMP ACCOUNT. IF ALREADY SUBSCRIBED, MESSAGE APPEARS
	form = EmailSignUpForm(request.POST or None)
	if request.method =='POST':
		if form.is_valid():
			email_signup_qs = Signup.objects.filter(email=form.instance.email)
			if email_signup_qs.exists():
				messages.info(request, 'You are already subscribed. Thank You!')
			else:
				subscribe(form.instance.email)
				form.save()
	return HttpResponseRedirect(request.META.get("HTTP_REFERER"))