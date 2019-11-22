from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name= 'post_list'),
    path('<id>, post_detail.html', views.post_detail, name='post_detail'),

    # path('<slug:slug>', views.post_detail, name='post_detail'),
    path('post_form.html', views.post_form, name='post_form'),
    path('post/<int:id>/edit', views.edit_post, name="edit_post"),
]
