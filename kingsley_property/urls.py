from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from listings.views import (
    listing_list, 
    listing_retrieve, 
    listing_create,
    listing_update,
    listing_delete,
    contact,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list, name='listings'),
    path('listings/<pk>/', listing_retrieve, name='listing'),
    path('listings/<pk>/edit', listing_update, name='update'),
    path('listings/<pk>/delete', listing_delete, name='delete'),
    path('add-listing/', listing_create, name= 'add'),
    path('contact/', contact, name='contact'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)