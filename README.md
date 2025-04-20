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

Generated on *Sun Apr 20 00:00:40 2025*:

```shell
yrouter is running...
Took 0.15776438899999334 seconds.

django is running...
Took 1.9941813030000048 seconds.

sanic is running...
Took 0.5136443160000113 seconds.

falcon is running...
Took 0.10316405699998654 seconds.

werkzeug is running...
Took 1.092525558999995 seconds.

```