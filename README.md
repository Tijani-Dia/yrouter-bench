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

Generated on *Sun Oct  8 00:00:53 2023*:

```shell
yrouter is running...
Took 0.2074717350000057 seconds.

django is running...
Took 2.804157191999998 seconds.

sanic is running...
Took 0.6520976179999991 seconds.

falcon is running...
Took 0.16334873199999578 seconds.

werkzeug is running...
Took 1.4393883550000055 seconds.

```