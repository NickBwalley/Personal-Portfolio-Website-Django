from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def home(request):
	if request.method == 'POST':
		form = UserReviewForm(request.POST)
		if form.is_valid():
			form.save()
			form1 = UserReviewForm()
			context1 = {'form': form1}

			return render(request, 'myportfolio/index.html', context1)
	form = UserReviewForm()
	context = {'form': form}
	return render(request, 'myportfolio/index.html', context)
    
