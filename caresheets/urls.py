from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
# from search import urls as urls_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls'))
    # path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    # path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    # path('search/', include(urls_search)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
