from django.urls import include, path, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    re_path(r'', include(router.urls)),
    path('handled_500_error', views.handled_500_error),
    path('unhandled_500_error', views.unhandled_500_error),
]
