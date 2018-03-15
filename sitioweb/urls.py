from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from biblioteca.views import  home,logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    url(r'^home/', home),
    url(r'^logout/$', logout_view),
]
