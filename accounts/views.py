from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(response, "registration/register.html", {"form": form})

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
