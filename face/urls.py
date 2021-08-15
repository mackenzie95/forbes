from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
        path('', views.face),
        path('get_data/', views.get_data),
        ]



urlpatterns += staticfiles_urlpatterns()
