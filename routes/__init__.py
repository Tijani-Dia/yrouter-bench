from django.urls import include, path, re_path
from yrouter import route

from .article_routes import routes as article_routes
from .article_routes import urlpatterns as article_urlpatterns
from .handlers import articles_handler, catchall, home_handler, users_handler
from .user_routes import routes as user_routes
from .user_routes import urlpatterns as user_urlpatterns

routes = (
    route("/", home_handler, name="home"),
    route(
        "articles/",
        articles_handler,
        name="articles_routes",
        subroutes=article_routes,
    ),
    route("users/", name="users_routes", subroutes=user_routes),
    route("<re:(?P<catched>^[a-z]*$)>/", catchall, name="catchall"),
    route("int/<int:id>", home_handler, name="int"),
)

urlpatterns = [
    path("", home_handler, name="home"),
    path(
        "articles/",
        include(article_urlpatterns),
    ),
    path("users/", include(user_urlpatterns)),
    re_path("(?P<catched>^[a-z]*$)>/", catchall, name="catchall"),
    path("int/<int:id>", home_handler, name="int"),
]

__all__ = ["routes", "urlpatterns"]
