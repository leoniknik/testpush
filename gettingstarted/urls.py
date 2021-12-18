from django.urls import path, include
import hello.views
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
    path('<str:room_name>/', hello.views.room, name='room'),
]
