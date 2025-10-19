# Yrouter-bench

The approach is to have the same URL configuration for [yrouter](https://github.com/Tijani-Dia/yrouter) and other routing modules and try to match some paths.

Currently, the benchmark is against `django`, `sanic`, `falcon` and `werkzeug`.

## How to run the benchmarks

1. Clone this repository

```shell
git clone https://github.com/Tijani-Dia/yrouter-bench.git
```

2. Install requirements

```shell
cd yrouter-bench
pip install -r requirements.txt
```

3. Run the benchmark

```shell
python bench.py
```

## Latest Results

A github action runs weekly and shows the latest benchmark results here.

Generated on *Sun Oct 19 00:00:57 2025*:

```shell
yrouter is running...
Took 0.14511563799999294 seconds.

django is running...
Took 1.9787847349999765 seconds.

sanic is running...
Took 0.4661643440000489 seconds.

falcon is running...
Took 0.12869593400000667 seconds.

werkzeug is running...
Took 0.9740731529999493 seconds.

```