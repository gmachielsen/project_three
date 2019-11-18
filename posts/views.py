from django.shortcuts import render, redirect, HttpResponse
from .forms import AnimalForm
from django.contrib import messages
from .models import Animal


def post_list(request):
    animals = Animal.objects.all()
    return render(request, 'posts/post_list.html', {'animals': animals})

def post_detail(request):
    return render(request, 'posts/post_detail.html', {})

# def post_form(request):
#     return render(request, 'posts/post_form.html', {})

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
