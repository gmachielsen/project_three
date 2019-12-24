from django.shortcuts import render
from posts.models import Animal

# Create your views here.


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
