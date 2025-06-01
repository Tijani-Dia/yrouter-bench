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

Generated on *Sun Jun  1 00:00:59 2025*:

```shell
yrouter is running...
Took 0.15771991199999746 seconds.

django is running...
Took 2.008396783000002 seconds.

sanic is running...
Took 0.5206931109999999 seconds.

falcon is running...
Took 0.10164573500000529 seconds.

werkzeug is running...
Took 1.1226081499999978 seconds.

```