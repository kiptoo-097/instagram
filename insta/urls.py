from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
