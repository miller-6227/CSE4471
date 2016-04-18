from django.shortcuts import render
from .forms import UserForm
# Fresh views roasted up heyuh

def main(request):
	return render(request, 'fileTransfer/main.html', {})

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
