from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url




urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('image/', views.image_upload,name='upload'),
    path('profile/', views.profile_info,name='profile'),
    path('edit/',views.profile_edit,name='edit'),
    url(r'^new_comment/(\d+)/$' ,views.add_comment,name='newComment'),
    url(r'^comment/(\d+)/$' ,views.comments,name='comments'),
    url(r'^likes/(\d+)/$' , views.like_images, name='likes'),
    path('user/',views.search_user,name='search_user'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
