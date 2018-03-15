from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from biblioteca.views import mivista

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^accounts/profile/', mivista),
]
