from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('author/', include('authors.urls')),
    path('posts/', include('posts.urls')),

]