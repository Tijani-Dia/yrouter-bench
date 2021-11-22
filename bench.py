from django.urls import resolve

from routes import sanic_router, y_router


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


if __name__ == "__main__":
    import timeit

    print("yrouter is running...")
    ytime = timeit.timeit("bench()", globals=globals(), number=10000)
    print(f"Took {ytime} seconds.\n")

    print("django is running...")
    djtime = timeit.timeit("bench_dj()", globals=globals(), number=10000)
    print(f"Took {djtime} seconds.\n")

    print("sanic is running...")
    sanic_time = timeit.timeit("bench_sanic()", globals=globals(), number=10000)
    print(f"Took {sanic_time} seconds.")
