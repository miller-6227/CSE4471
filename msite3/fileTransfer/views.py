from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from .forms import UserForm
from fileTransfer.models import Document
from fileTransfer.forms import DocumentForm


# Fresh views roasted up heyuh

def main(request):
	return render(request, 'fileTransfer/main.html', {})

def list(request):
# File upload
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()

			#redirect to list/main
			return HttpResponseRedirect(reverse('fileTransfer.views.list'))

	else:
		form = DocumentForm()

	#all documents beings populated...
	documents = Document.objects.all()

	# Render main page
	return render(request, 'fileTransfer/list.html',
		{'documents':documents, 'form': form})

def create(request):
	form=UserForm()

	if request.method=="POST":
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.save()
	return render(request, 'fileTransfer/create.html', {'form':form})

def about(request):
	return render(request, 'fileTransfer/about.html', {})

def sendFile(request):
        return render(request, 'fileTransfer/sendFile.html', {})
