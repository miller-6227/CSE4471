from django.shortcuts import render

# Fresh views roasted up heyuh

def main(request):
	return render(request, 'fileTransfer/main.html', {})

def create(request):
	return render(request, 'fileTransfer/create.html', {})

def about(request):
	return render(request, 'fileTransfer/about.html', {})