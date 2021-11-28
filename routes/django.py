from django.urls import include, path, re_path

from . import handlers

article_urlpatterns = [
    path("2020/", handlers.handler_2020, name="articles-2020"),
    path(
        "categories/",
        include(
            [
                path("<str:category>", handlers.category, name="categories"),
                path(
                    "<str:category>/newest/", handlers.newest, name="newest-in-category"
                ),
            ]
        ),
    ),
    path("<int:year>/", handlers.year_handler, name="articles-year"),
    path("<int:year>/<int:month>/", handlers.month_handler, name="articles-year-month"),
    path("<int:year>/popular/", handlers.month_handler, name="articles-year-month"),
    path(
        "<int:year>/<int:month>/<int:day>/",
        handlers.popular_articles,
        name="popular-articles",
    ),
]

user_urlpatterns = [path("extra/", handlers.home_handler, name="users-extra")]


urlpatterns = [
    path("", handlers.home_handler, name="home"),
    path(
        "articles/",
        include(article_urlpatterns),
    ),
    path("users/", include(user_urlpatterns)),
    re_path("^[a-z]*$", handlers.catchall, name="catchall"),
    path("int/<int:id>", handlers.home_handler, name="int"),
]
