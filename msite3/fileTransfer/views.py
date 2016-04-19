from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from fileTransfer.models import Document, Transfer

from .forms import UserForm
from fileTransfer.models import Document
from fileTransfer.forms import DocumentForm
from django.views.generic import View
from django.template import loader

from .core import server, client

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
			return HttpResponseRedirect('/fileTransfer/')



	return render(request, 'fileTransfer/create.html', {'form':form})

def about(request):
	return render(request, 'fileTransfer/about.html', {})

class SenderView(View):

    template_name = 'fileTransfer/sendFile.html'
    open_file = ''

    def get(self, request, *args, **kwargs):
        form = DocumentForm()
        documents = Document.objects.all()
        return render(self.request, self.template_name, {'documents':documents, 'form': form})

    def post(self, request, *args, **kwargs):
        # File upload
        if self.request.method == 'POST':
            form = DocumentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                self.open_file = Document(docfile = self.request.FILES['docfile'])
                self.open_file.save()
                #redirect to sendFile/main
                return HttpResponseRedirect('.')
        else:
            form = DocumentForm()
        #all documents beings populated...
        documents = Document.objects.all()
        # Render main page
        return render(self.request, self.template_name, {'documents':documents, 'form': form})

    def sendFile(self, request):
        s = Transfer.sender(self.ip, self.port)
        if self.open_file != '': s.send_file(self.open_file)
