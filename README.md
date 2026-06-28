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

Generated on *Sun Jun 28 00:18:36 2026*:

```shell
yrouter is running...
Took 0.149518331000003 seconds.

django is running...
Took 1.8023546870000047 seconds.

sanic is running...
Took 0.47614980999999545 seconds.

falcon is running...
Took 0.11893180599999909 seconds.

werkzeug is running...
Took 1.0052593549999997 seconds.

```