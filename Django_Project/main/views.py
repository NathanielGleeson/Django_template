from django.shortcuts import render, redirect



def index(request):
	return render(request, 'main/index.html')

def components(request):
	return render(request, 'main/components.html')

def about(request):
	return render(request, 'main/about.html')

def contact(request):
	return render(request, 'main/contact.html')

def works(request):
	return render(request, 'main/works.html')

def work(request):
	return render(request, 'main/work.html')