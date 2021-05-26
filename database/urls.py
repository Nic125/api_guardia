from django.conf.urls import url
from database import views

urlpatterns = [
    url(r'^department/$', views.department),
    url(r'^department/([0-9]+)$', views.department),
    url(r'^service/$', views.service),
    url(r'^service/([0-9]+)$', views.service),
    url(r'^guard/$', views.guard),
    url(r'^guard/([0-9]+)$', views.guard),
    url(r'^personal/$', views.personal),
    url(r'^personal/([0-9]+)$', views.personal),
    url(r'^guard_sheets/$', views.guard_sheet),
    url(r'^guard_sheets/([0-9]+)$', views.guard_sheet),
]