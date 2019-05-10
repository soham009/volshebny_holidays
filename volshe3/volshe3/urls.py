from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from generateletter import views

urlpatterns = [
    path("", include("generateletter.urls")),
    path("admin/", admin.site.urls),
]

handler404 = views.error_404
handler500 = views.error_500