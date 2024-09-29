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

Generated on *Sun Sep 29 00:00:54 2024*:

```shell
yrouter is running...
Took 0.16321356700001388 seconds.

django is running...
Took 2.0851472569999885 seconds.

sanic is running...
Took 0.5302527139999995 seconds.

falcon is running...
Took 0.10042620100000477 seconds.

werkzeug is running...
Took 1.1375936799999806 seconds.

```