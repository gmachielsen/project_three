from django.shortcuts import render, redirect, HttpResponse
from .forms import AnimalForm

def post_list(request):
    return render(request, 'posts/post_list.html', {})

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
            return redirect('add_animal')

        else:
            messages.error(request, ("animalcaresheet is NOT been added, please try again"))
            # return redirect('post_form')
            return render(request, 'posts/post_form.html', {'form': form})
    else:
        form = AnimalForm()
        return render(request, 'posts/post_form.html', {'form': form})
