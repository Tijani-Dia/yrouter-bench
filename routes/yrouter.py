from yrouter import Router, route

from . import handlers

article_routes = (
    route("2020/", handlers.handler_2020, name="articles-2020"),
    route(
        "categories/",
        handlers.article_categories,
        name="categories",
        subroutes=(
            route(
                "<str:category>",
                handlers.category,
                subroutes=(
                    route("newest/", handlers.newest, name="newest-in-category"),
                ),
            ),
        ),
    ),
    route(
        "<int:year>/",
        handlers.year_handler,
        name="articles-year",
        subroutes=(
            route(
                "<int:month>/",
                handlers.month_handler,
                name="articles-year-month",
                subroutes=(
                    route(
                        "<int:day>/",
                        handlers.day_handler,
                        name="articles-year-month-day",
                    ),
                ),
            ),
            route(
                "popular",
                handlers.popular_articles,
                name="popular-articles",
            ),
        ),
    ),
)

user_routes = (route("extra/", handlers.home_handler, name="users-extra"),)

routes = (
    route("/", handlers.home_handler, name="home"),
    route(
        "articles/",
        handlers.articles_handler,
        name="articles_routes",
        subroutes=article_routes,
    ),
    route("users/", name="users_routes", subroutes=user_routes),
    route("<re:(?P<catched>^[a-z]*$)>/", handlers.catchall, name="catchall"),
    route("int/<int:id>", handlers.home_handler, name="int"),
)

y_router = Router(routes)
