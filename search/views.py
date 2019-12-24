from django.shortcuts import render
from posts.models import Animal

# Create your views here.


def do_search(request):
    posts = Animal.objects.filter(name__icontains=request.GET['q'])
    return render(request, "product_list.html", {"posts": posts})
