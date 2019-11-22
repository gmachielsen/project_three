from django.shortcuts import render, redirect, HttpResponse
from .forms import AnimalForm
from django.contrib import messages
from .models import Animal, AnimalImages

from django.views.generic.detail import DetailView



def post_list(request):
    animals = Animal.objects.all()
    return render(request, 'posts/post_list.html', {'animals': animals})

def post_detail(request, id):
    animal = Animal.objects.get(pk=id)
    slug = animal
    # slug = Animal.kwargs.get('slug')
    # animal = Animal.objects.get(slug=slug)
# def post_detail(request, id):
    # animal = Animal.objects.get(pk=slug)
    # animal_images = AnimalImages.objects.filter(pk=slug)

    # animal = Animal.objects.get(pk=id)
    # animal_images = AnimalImages.objects.filter(pk=id)
    # return render(request, 'posts/post_detail.html', {"animal": animal, "animal_images": animal_images})
    return render(request, 'posts/post_detail.html', {"animal": animal, "slug": slug })


def post_form(request):

    if request.method == 'POST':
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, ("animalcaresheet successfully added"))
            return redirect('post_list')

        else:
            messages.error(request, ("animalcaresheet is NOT been added, please try again"))
            # return redirect('post_form')
            return render(request, 'posts/post_form.html', {'form': form})
    else:
        form = AnimalForm()
        return render(request, 'posts/post_form.html', {'form': form})


def edit_post(request, id):
    # Load the post we're changing, from the DB
    post = Animal.objects.get(Animal, pk=id)

    if request.method == "POST":
        form = AnimalForm(request.Animal, request.FILES, instance=post)
        return update_post(form)
    else:
        form = Animal(instance=post)
        return render(request, "posts/post_form.html", {"form": form})


def update_post(form):
    # Update the DB with the differences
    if form.is_valid():
        post = form.save()
        return redirect("post_detail", id=post.id)
    else:
        return render(request, "posts/post_form.html", {"form": form})
