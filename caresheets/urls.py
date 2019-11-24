from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
