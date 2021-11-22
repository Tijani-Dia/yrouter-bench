from django.urls import include, path, re_path, set_urlconf
from sanic_routing import BaseRouter
from yrouter import Router, route

from .article_routes import routes as article_routes
from .article_routes import urlpatterns as article_urlpatterns
from .handlers import (
    articles_handler,
    catchall,
    category,
    day_handler,
    handler_2020,
    home_handler,
    month_handler,
    newest,
    popular_articles,
    users_handler,
    year_handler,
)
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
    re_path("^[a-z]*$", catchall, name="catchall"),
    path("int/<int:id>", home_handler, name="int"),
]


class SanicRouter(BaseRouter):
    def get(self, path, *args, **kwargs):
        return self.resolve(path, *args, **kwargs)


sanic_router = SanicRouter()

sanic_router.add("/", home_handler)
sanic_router.add("/articles", articles_handler)
sanic_router.add("/articles/2020", handler_2020)
sanic_router.add("/articles/categories/<category:str>", category)
sanic_router.add("/articles/categories/<category:str>/newest/", newest)
sanic_router.add("/articles/<year:int>", year_handler)
sanic_router.add("/articles/<year:int>/<month:int>", month_handler)
sanic_router.add("/articles/<year:int>/popular", popular_articles)
sanic_router.add("/articles/<year:int>/<month:int>/<day:int>", day_handler)
sanic_router.add("/users/extra", users_handler)
sanic_router.add("<catchall>", users_handler)
sanic_router.add("/int/<id:int>", home_handler)

sanic_router.finalize()
y_router = Router(routes)
set_urlconf("routes.__init__")

__all__ = ["routes", "urlpatterns", "sanic_router"]
