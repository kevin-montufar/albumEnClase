from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category

# Create your views here.

def first_view(request):
    return HttpResponse('<h1> al fin una  vista </h1>')

def category(request):
	category_list = Category.objects.all()
	context = {'object_list': category_list}
	return render(request, 'album/category.html', context)
