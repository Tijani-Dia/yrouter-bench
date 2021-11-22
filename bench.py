from django.urls import resolve, set_urlconf
from yrouter import Router

from routes import routes


def bench():
    router = Router(routes)
    router.match("/")
    router.match("/articles/2020/")
    router.match("/articles/2015/")
    router.match("/articles/2015/04/12/")
    router.match("/articles/categories/sport/newest/")
    router.match("/users/extra")

    router.match("/articles/2015/04/12/98/")
    router.match("/users/extra/bog")


def bench_dj():
    set_urlconf("routes.__init__")
    resolve("/")
    resolve("/articles/2020/")
    resolve("/articles/2015/")
    resolve("/articles/2015/04/12/")
    resolve("/articles/categories/sport/newest/")
    resolve("/users/extra/")

    try:
        resolve("/articles/2015/04/12/98/")
    except:
        pass

    try:
        resolve("/users/extra/bog")
    except:
        pass


if __name__ == "__main__":
    import timeit

    print("yrouter is running...")
    ytime = timeit.timeit("bench()", globals=globals(), number=10000)
    print(f"Took {ytime} seconds.\n")

    print("django is running...")
    djtime = timeit.timeit("bench_dj()", globals=globals(), number=10000)
    print(f"Took {djtime} seconds.")
