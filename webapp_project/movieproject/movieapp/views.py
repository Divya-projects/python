from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()

    return render(request,'index.html', {'context': movie})

def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    # return HttpResponse('This is movie no %s' % movie_id)
    return render(request,'detail.html',{'movie': movie})

def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('description')
        year = request.POST.get('year')
        image = request.FILES['image']
        movie = Movie(name=name,desc=desc,year=year,img=image)
        movie.save()

    return render(request,'add.html')

def update(request,id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form': form, 'movie': movie})
    # form = MovieForm(request.POST, request.FILES, instance=Movie.objects.get(id=id))
    # return render(request, 'edit.html',{'form': form})

def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
