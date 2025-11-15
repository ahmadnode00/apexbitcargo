from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from tracking import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),      # Admin
    path('', include('tracking.urls')),   # App URLs (homepage included here)
    path('about/', views.about, name='about'),  # About page
]

# Media (image serving)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
