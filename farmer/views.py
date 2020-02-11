from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from profiles.models import User
from dealer.models import Post_advertise 
from django.conf import settings
import datetime
from .forms import AddContactusForm


# Create your views here.


def showad(request):
	viewad = Post_advertise.objects.filter().order_by('-created_at')
	return render(request, 'advertisement.html', {'viewad': viewad})


def addcontactus(request):
	if request.method == 'POST':
		form = AddContactusForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'contactus.html')

	else:
		form = AddContactusForm()
	return render(request,'contactus.html',{'form':form})
