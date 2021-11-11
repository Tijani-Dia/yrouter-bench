from django.urls import include, path, re_path
from yrouter import route

from .handlers import (
    article_categories,
    category,
    day_handler,
    handler_2020,
    month_handler,
    newest,
    popular_articles,
    year_handler,
)

routes = (
    route("2020/", handler_2020, name="articles-2020"),
    route(
        "categories/",
        article_categories,
        name="categories",
        subroutes=(
            route(
                "<str:category>",
                category,
                subroutes=(route("newest/", newest, name="newest-in-category"),),
            ),
        ),
    ),
    route(
        "<int:year>/",
        year_handler,
        name="articles-year",
        subroutes=(
            route(
                "<int:month>/",
                month_handler,
                name="articles-year-month",
                subroutes=(
                    route(
                        "<int:day>/",
                        day_handler,
                        name="articles-year-month-day",
                    ),
                ),
            ),
            route(
                "popular",
                popular_articles,
                name="popular-articles",
            ),
        ),
    ),
)

urlpatterns = [
    path("2020/", handler_2020, name="articles-2020"),
    path(
        "categories/",
        include(
            [
                path("<str:category>", category, name="categories"),
                path("<str:category>/newest/", newest, name="newest-in-category"),
            ]
        ),
    ),
    path("<int:year>/", year_handler, name="articles-year"),
    path("<int:year>/<int:month>/", month_handler, name="articles-year-month"),
    path("<int:year>/popular/", month_handler, name="articles-year-month"),
    path(
        "<int:year>/<int:month>/<int:day>/", popular_articles, name="popular-articles"
    ),
]
