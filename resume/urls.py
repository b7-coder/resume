from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('download_resume/', download_resume, name='download_resume'),
    path('blogDetails/<int:id>', blogDetails, name='blogDetails'),
    path('comments/<int:id>', comments, name='comments'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root = settings.MEDIA_ROOT)