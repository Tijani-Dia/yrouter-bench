from falcon.routing import DefaultRouter


class ResourceWithId:
    def __init__(self, resource_id):
        self.resource_id = resource_id

    def __repr__(self):
        return "ResourceWithId({})".format(self.resource_id)

    def on_get(self, req, resp):
        resp.text = self.resource_id


def make_router():
    router = DefaultRouter()

    router.add_route("/", ResourceWithId(1))
    router.add_route("/articles", ResourceWithId(2))
    router.add_route("/articles/2020/", ResourceWithId(3))
    router.add_route("/articles/categories/{category}", ResourceWithId(4))
    router.add_route("/articles/categories/{category}/newest/", ResourceWithId(5))
    router.add_route("/articles/{year:int}/", ResourceWithId(6))
    router.add_route("/articles/{year:int}/{month:int}", ResourceWithId(7))
    router.add_route("/articles/{year:int}/popular", ResourceWithId(8))
    router.add_route("/articles/{year:int}/{month:int}/{day:int}/", ResourceWithId(9))
    router.add_route("/users/extra", ResourceWithId(10))
    router.add_route("/{catchall}", ResourceWithId(11))
    router.add_route("/int/{id:int}", ResourceWithId(11))

    return router


falcon_router = make_router()
