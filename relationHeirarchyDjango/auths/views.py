from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



def register(request):
	import os.path
	# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
	os.chdir('..')
	print("h","klfdksjfsdkjlf")
	from core import models as core_models
	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']
		email = request.POST['email']
		User.objects.create_user(username, email, password)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			core_models.UserPairs.objects.create(user = user)
			up = core_models.UserPairs.objects.get(user=user)
			# for tup in core_models.Tuple.objects.all():
			up.tuples.add(*list(core_models.Tuple.objects.all()))
			up.save()

		else:
			return render(request, 'auths/signup.html')
		
		messages.success(request,f'Account created for {username}!')
		return redirect('core:home')
	else:
		return render(request, 'auths/signup.html')



	
