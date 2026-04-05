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

Generated on *Sun Apr  5 00:04:20 2026*:

```shell
yrouter is running...
Took 0.15821802699999665 seconds.

django is running...
Took 2.0135083710000004 seconds.

sanic is running...
Took 0.507334200999999 seconds.

falcon is running...
Took 0.12925887299999772 seconds.

werkzeug is running...
Took 1.1400394710000015 seconds.

```