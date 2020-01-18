from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from portal.views import *


urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('sndex/', Hei),
    path('', Register),
    path('calendar/', calendar),
    path('index/', index)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)