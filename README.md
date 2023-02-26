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

Generated on *Sun Feb 26 00:33:39 2023*:

```shell
yrouter is running...
Took 0.19903439600000183 seconds.

django is running...
Took 2.66271352199999 seconds.

sanic is running...
Took 0.6297307950000004 seconds.

falcon is running...
Took 0.15747179900000674 seconds.

werkzeug is running...
Took 1.4863920930000063 seconds.

```