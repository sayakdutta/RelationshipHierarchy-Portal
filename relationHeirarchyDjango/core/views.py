from django.shortcuts import render, redirect
import os
from django.conf import settings
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum

# def temp(request):


# 	file = open(os.path.join(settings.BASE_DIR, 'parent-child-pairs.csv'))

# 	filecontent = file.readlines()
# 	for line in filecontent:
# 		rels = line.strip().split(",")
# 		Tuple.objects.create(parent = rels[0], child = rels[1])



# 	return render(request,'core/download.html')

# def init_copy():
# 	tuples = Tuple.objects.all().order_by('sump')
# 	for i in range(1,len(tuples)+1):
# 		TupleCopy.objects.create(id=i, parent=tuples[i-1].parent, child=tuples[i-1].child, sump=tuples[i-1].pos+tuples[i-1].neg)

# 	print("DONE", "XXXXXXXXXXXXXXx")

# def getKTuples(k):
# 	startIndex = RangeIndex.objects.all()[0]
# 	tuples = TupleCopy.objects.all()[startIndex:startIndex+k]

# 	return tuples

# def addMore(start, end):
# 	tuples = Tuple.objects.all().order_by('sump')
# 	for i in range(1,len(tuples)+1):
# 		TupleCopy.objects.create(id=i, parent=tuples[i-1].parent, child=tuples[i-1].child, sump=tuples[i-1].pos+tuples[i-1].neg)

# 	print("DONE", "XXXXXXXXXXXXXXx")

@login_required
def verify(request):
	if request.method == 'POST':
		pk=0
		for key in request.POST:
			if key != 'csrfmiddlewaretoken':
				pk = int(key[6:])
				tupl = Tuple.objects.get(pk=pk)
				if request.POST[key] == "Yes":
					tupl.pos += 1 
				elif request.POST[key] == "No":
					tupl.neg += 1
				tupl.sump += 1
				request.user.pairs.tuples.remove(tupl)

				tupl.save()
				print(pk, request.POST[key])
		request.user.pairs.verifyNumber += 10
		request.user.pairs.save()
		# startIndex = RangeIndex.objects.all()[0]
		# startIndex.startIndex = pk+1
		# startIndex.save()

		return redirect('core:verify')
	else:
		# tuples = getKTuples(10)
		tuples = request.user.pairs.tuples.order_by('sump')[:10]
		# tuples = Tuple.objects.all().annotate(total_votes=Sum(F('pos') + F('neg'))).order_by('total_votes')[:10]

		context = {
			'activate': 'verheir',
			'tuples' : tuples,
		}
		

		return render(request, 'core/verify.html', context)
