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

Generated on *Sun Feb  9 00:00:49 2025*:

```shell
yrouter is running...
Took 0.155200985999997 seconds.

django is running...
Took 1.9603492060000036 seconds.

sanic is running...
Took 0.5176164209999996 seconds.

falcon is running...
Took 0.10459815899999114 seconds.

werkzeug is running...
Took 1.1422118659999967 seconds.

```