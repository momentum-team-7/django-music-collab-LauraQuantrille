"""djangomusic URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views 
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.album_list, name='home'),
    path('artists/', views.artist_list, name='artists',),
    path('albums/<int:pk>/details/', views.album_detail, name='album-detail'),
    path('artist-list/<int:pk>/details/', views.artist_detail, name='artist-detail'),
    path('artists/new', views.add_artist, name='add-artist'),
    path('albums/new', views.add_album, name='add-album'),
    path('artists/<int:pk>/edit', views.edit_artist, name="edit-artist"),
    path('artists/<int:pk>/delete', views.delete_artist, name="delete-artist"),
    path('albums/<int:pk>/edit', views.edit_album, name="edit-album"),
    

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    if settings.DEBUG: # new
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
