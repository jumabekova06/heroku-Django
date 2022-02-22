from django.contrib import admin
from django.urls import path
from itcoder.views import my_main_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_main_page),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

