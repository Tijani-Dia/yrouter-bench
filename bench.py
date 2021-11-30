from django.urls import resolve, set_urlconf

from routes.falcon import falcon_router
from routes.sanic import sanic_router
from routes.werkzeug import werkzeug_router
from routes.yrouter import y_router


def bench():
    y_router.match("/")
    y_router.match("/articles/2020/")
    y_router.match("/articles/2015/")
    y_router.match("/articles/2015/04/12/")
    y_router.match("/articles/categories/sport/newest/")
    y_router.match("/users/extra")
    y_router.match("catchall")
    y_router.match("/int/92")

    y_router.match("/articles/2015/04/12/98/")
    y_router.match("/users/extra/bog")


def bench_dj():
    resolve("/")
    resolve("/articles/2020/")
    resolve("/articles/2015/")
    resolve("/articles/2015/04/12/")
    resolve("/articles/categories/sport/newest/")
    resolve("/users/extra/")
    resolve("/catchall")
    resolve("/int/92")

    try:
        resolve("/articles/2015/04/12/98/")
    except:
        pass

    try:
        resolve("/users/extra/bog")
    except:
        pass


def bench_sanic():
    sanic_router.get("/", method="BASE")
    sanic_router.get("/articles/2020/", method="BASE")
    sanic_router.get("/articles/2015/", method="BASE")
    sanic_router.get("/articles/2015/04/12/", method="BASE")
    sanic_router.get("/articles/categories/sport/newest/", method="BASE")
    sanic_router.get("/users/extra", method="BASE")
    sanic_router.get("/catchall", method="BASE")
    sanic_router.get("/int/92", method="BASE")

    try:
        sanic_router.get("/articles/2015/04/12/98/", method="BASE")
    except:
        pass
    try:
        sanic_router.get("/users/extra/bog", method="BASE")
    except:
        pass


def bench_falcon():
    falcon_router.find("/")
    falcon_router.find("/articles/2020/")
    falcon_router.find("/articles/2015/")
    falcon_router.find("/articles/2015/04/12/")
    falcon_router.find("/articles/categories/sport/newest/")
    falcon_router.find("/users/extra")
    falcon_router.find("/catchall")
    falcon_router.find("/int/92")

    falcon_router.find("/articles/2015/04/12/98")
    falcon_router.find("/users/extra/bog")


def bench_werkzeug():
    werkzeug_router.match("/")
    werkzeug_router.match("/articles/2020/")
    werkzeug_router.match("/articles/2015/")
    werkzeug_router.match("/articles/2015/04/12/")
    werkzeug_router.match("/articles/categories/sport/newest/")
    werkzeug_router.match("/users/extra/")
    werkzeug_router.match("/catchall/")
    werkzeug_router.match("/int/92/")

    try:
        werkzeug_router.match("/articles/2015/04/12/98")
    except:
        pass
    try:
        werkzeug_router.match("/users/extra/bog")
    except:
        pass


if __name__ == "__main__":
    import timeit

    set_urlconf("routes.django")

    print("yrouter is running...")
    ytime = timeit.timeit("bench()", globals=globals(), number=10000)
    print(f"Took {ytime} seconds.\n")

    print("django is running...")
    djtime = timeit.timeit("bench_dj()", globals=globals(), number=10000)
    print(f"Took {djtime} seconds.\n")

    print("sanic is running...")
    sanic_time = timeit.timeit("bench_sanic()", globals=globals(), number=10000)
    print(f"Took {sanic_time} seconds.\n")

    print("falcon is running...")
    falcon_time = timeit.timeit("bench_falcon()", globals=globals(), number=10000)
    print(f"Took {falcon_time} seconds.\n")

    print("werkzeug is running...")
    werkzeug_time = timeit.timeit("bench_werkzeug()", globals=globals(), number=10000)
    print(f"Took {werkzeug_time} seconds.\n")
