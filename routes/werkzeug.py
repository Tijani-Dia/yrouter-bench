from werkzeug import routing

_map = routing.Map(
    [
        routing.Rule("/", endpoint="home_handler"),
        routing.Rule("/articles/", endpoint="articles_handler"),
        routing.Rule("/articles/2020/", endpoint="handler_2020"),
        routing.Rule("/articles/categories/<category>/", endpoint="category"),
        routing.Rule("/articles/categories/<category>/newest/", endpoint="newest"),
        routing.Rule("/articles/<int:year>/", endpoint="year_handler"),
        routing.Rule("/articles/<int:year>/<int:month>/", endpoint="month_handler"),
        routing.Rule("/articles/<int:year>/popular/", endpoint="popular_articles"),
        routing.Rule(
            "/articles/<int:year>/<int:month>/<int:day>/", endpoint="day_handler"
        ),
        routing.Rule("/users/extra/", endpoint="users_handler"),
        routing.Rule("/<catchall>/", endpoint="users_handler"),
        routing.Rule("/int/<int:id>/", endpoint="home_handler"),
    ]
)

werkzeug_router = _map.bind("example.org", "/")
