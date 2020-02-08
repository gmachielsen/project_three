from django.shortcuts import render, redirect, HttpResponse
from .forms import AnimalForm, AnimalTypeForm
from django.contrib import messages
from .models import Animal, AnimalImages
from django.db.models import Q


def index(request):
    animals = Animal.objects.all().order_by('-created')
    return render(request, 'posts/index.html', {"animals": animals})

def is_valid_param(param):
    return param is not '' and param is not None

def post_list(request):
    search_term=''
    animals = Animal.objects.all().order_by('latinName')
    # reptiles = Animal.objects.all()
    filter = AnimalTypeForm(request.GET)
    print(filter)
    if ('search' in request.GET):
        search_term = request.GET['search']
        animals = animals.filter(latinName__icontains=search_term)
    elif('reptiletype' in request.GET and 'reptiletype' != 'X'):
        type = request.GET.get('reptiletype')
        animals = animals.filter(reptiletype=type)
    else:
        animals = Animal.objects.all().order_by('latinName')
        
    return render(request, 'posts/post_list.html', {'animals': animals, 'search_term': search_term, "filter": filter})


def post_detail(request, id):
    animal = Animal.objects.get(pk=id)
    animal.views +=1
    animal.save()
    return render(request, 'posts/post_detail.html', {"animal": animal})


def post_form(request):

    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, ("animalcaresheet successfully added"))
            return redirect('post_list')

        else:
            messages.error(request, ("animalcaresheet is NOT been added, please try again"))
            # return redirect('post_form')
            return render(request, 'posts/post_form.html', {'form': form})
    else:
        form = AnimalForm()
        return render(request, 'posts/post_form.html', {'form': form})

def delete_post(request, id):
    animal = Animal.objects.get(pk=id)
    animal.delete()
    messages.success(request, ("animalcaresheet successfully deleted"))
    return redirect('post_list')

def edit_post(request, id):
    animal = Animal.objects.get(pk=id)
    form = AnimalForm(instance=animal, data=request.GET, files=request.FILES)

    if request.method=="POST":
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = AnimalForm(instance=animal)

    return render(request, "posts/edit_post.html", {'form': form})

def like_post(request, id):
    post = Animal.objects.get(pk=id)
    post.likes +=1
    post.save()
    return redirect("post_detail", id=post.id)


def dislike_post(request, id):
    post = Animal.objects.get(pk=id)
    post.dislikes +=1
    post.save()
    return redirect("post_detail", id=post.id)
