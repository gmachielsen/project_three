# from django.contrib.auth.models import User
# from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from posts.forms import AnimalForm
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from posts.models import Animal

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password1 = form.cleaned_data.get('password1')
            raw_password2 = form.cleaned_data.get('password2')

            user = authenticate(username=username, password=raw_password1)
            login(request, user)

        return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def profile(request):
    animal_caresheets = Animal.objects.all()
    return render(request, "profile/profile.html", {"animal_caresheets": animal_caresheets})





# def login(request):
#     if request.method == 'POST':
#         login = AuthenticationForm(request.POST)
#         if login.is_valid():
#             user = login.get_user()
#             login(request, user)
#             return redirect('posts:post_list.html')
#     else:
#         login = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'login': login})
# def login(response):
#     if user.is_authenticated:
#         return redirect('post_list')
#     else:
#         return render(response, "registration/login.html", {"form": form})
