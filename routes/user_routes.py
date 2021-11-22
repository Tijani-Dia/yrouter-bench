from django.urls import path
from yrouter import route

from .handlers import home_handler

routes = (route("extra/", home_handler, name="users-extra"),)
urlpatterns = [path("extra/", home_handler, name="users-extra")]
