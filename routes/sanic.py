from sanic_routing import BaseRouter

from . import handlers


class SanicRouter(BaseRouter):
    def get(self, path, *args, **kwargs):
        return self.resolve(path, *args, **kwargs)


sanic_router = SanicRouter()

sanic_router.add("/", handlers.home_handler)
sanic_router.add("/articles", handlers.articles_handler)
sanic_router.add("/articles/2020", handlers.handler_2020)
sanic_router.add("/articles/categories/<category:str>", handlers.category)
sanic_router.add("/articles/categories/<category:str>/newest/", handlers.newest)
sanic_router.add("/articles/<year:int>", handlers.year_handler)
sanic_router.add("/articles/<year:int>/<month:int>", handlers.month_handler)
sanic_router.add("/articles/<year:int>/popular", handlers.popular_articles)
sanic_router.add("/articles/<year:int>/<month:int>/<day:int>", handlers.day_handler)
sanic_router.add("/users/extra", handlers.users_handler)
sanic_router.add("<catchall>", handlers.users_handler)
sanic_router.add("/int/<id:int>", handlers.home_handler)

sanic_router.finalize()
