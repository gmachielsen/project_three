from django.shortcuts import render, redirect, HttpResponse


def post_list(request):
    return render(request, 'posts/post_list.html', {})


def post_detail(request):
    return render(request, 'posts/post_detail.html', {})

def post_form(request):
    return render(request, 'posts/post_form.html', {})
