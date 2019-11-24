from django.shortcuts import render, redirect, HttpResponse
from .forms import AnimalForm, AnimalSearchForm
from django.contrib import messages
from .models import Animal, AnimalImages
from django.db.models import Q
# from django.views.generic.detail import DetailView



def post_list(request):
    animals = Animal.objects.all()
    search_form = AnimalSearchForm()
    return render(request, 'posts/post_list.html', {'animals': animals, 'search_form': search_form})

def filter_posts_list(request):
    animals = Animal.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']

        query_by_name = Q(name__contains=search)
        query_by_description = Q(description__contains=search)

        animals = animals.filter(query_by_name | query_by_description)

        search_form = AnimalSearchForm(request.GET)
    return render(request, "posts/filter_post.html", {'animals': animals, 'search_form': search_form})

def post_detail(request, id):
    animal = Animal.objects.get(pk=id)
    # slug = Animal.kwargs.get('slug')
    # animal = Animal.objects.get(slug=slug)
# def post_detail(request, id):
    # animal = Animal.objects.get(pk=slug)
    # animal_images = AnimalImages.objects.filter(pk=slug)

    # animal = Animal.objects.get(pk=id)
    # animal_images = AnimalImages.objects.filter(pk=id)
    # return render(request, 'posts/post_detail.html', {"animal": animal, "animal_images": animal_images})
    return render(request, 'posts/post_detail.html', {"animal": animal})


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

def delete_post(request, id):
    animal = Animal.objects.get(pk=id)
    animal.delete()
    messages.success(request, ("animalcaresheet successfully deleted"))
    return redirect('post_list')

def edit_post(request, id):
    animal = Animal.objects.get(pk=id)
    form = AnimalForm(instance=animal, data=request.GET, files=request.FILES)

    if request.method=="POST":
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect(post_list)
    else:
        form = AnimalForm(instance=animal)

    return render(request, "posts/edit_post.html", {'form': form})

# def edit_post(request):
#     # Load the post we're changing, from the DB
#     animal = Animal.objects.get(pk=id)
#     form = AnimalForm(instance=animal, data=request.GET, files=request.FILES)
#
#     print('Files : {}'.format(request.Files))
#     if request.method == "POST":
#         form = AnimalForm(instance=animal, data=request.GET, files=request.FILES)
#         return update_post(form)
#     else:
#         raise(error)
#     return render(request, "posts/edit_post.html", {"form": form})


# def update_post(form):
#     # Update the DB with the differences
#     if form.is_valid():
#         post = form.save()
#         return redirect("post_detail", id=post.id)
#     else:
#         return render(request, "posts/post_form.html", {"form": form})
