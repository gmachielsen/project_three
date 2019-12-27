from django.urls import path
from . import views

urlpatterns = [
    path('list', views.post_list, name= 'post_list'),
    path('', views.index, name= 'index'),
    path('<id>, post_detail.html', views.post_detail, name='post_detail'),
    # path('<slug:slug>', views.post_detail, name='post_detail'),
    path('post_form.html', views.post_form, name='post_form'),
    path('post/<id>/edit', views.edit_post, name="edit_post"),
    path('post/<id>/delete', views.delete_post, name="delete_post"),
    path('post/<int:id>/like', views.like_post, name="like_post"),
    path('post/<int:id>/dislike', views.dislike_post, name="dislike_post"),
    # path("", views.do_search, name="search")
        # path('filter/', filter_product_list, name='filter_product_list'),

]
