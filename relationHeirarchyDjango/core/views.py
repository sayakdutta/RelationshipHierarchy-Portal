from django.shortcuts import render, redirect
import os
from django.conf import settings
from .models import *
from django.contrib.auth.decorators import login_required

# def temp(request):


# 	file = open(os.path.join(settings.BASE_DIR, 'parent-child-pairs.csv'))

# 	filecontent = file.readlines()
# 	for line in filecontent:
# 		rels = line.strip().split(",")
# 		Tuple.objects.create(parent = rels[0], child = rels[1])



# 	return render(request,'core/download.html')

@login_required
def verify(request):
	if request.method == 'POST':
		
		for key in request.POST:
			if key != 'csrfmiddlewaretoken':
				pk = int(key[6:])
				tupl = Tuple.objects.get(pk=pk)
				if request.POST[key] == "Yes":
					tupl.pos += 1 
				elif request.POST[key] == "No":
					tupl.neg += 1
				tupl.save()
				print(pk, request.POST[key])

		return redirect('core:home')
	else:
		tuples = Tuple.objects.all()[:10]

		context = {
			'activate': 'verheir',
			'tuples' : tuples,
		}
		

		return render(request, 'core/verify.html', context)
