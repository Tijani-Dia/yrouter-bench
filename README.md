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

Generated on *Sun Sep 21 00:00:50 2025*:

```shell
yrouter is running...
Took 0.1525798750000007 seconds.

django is running...
Took 2.2533502510000005 seconds.

sanic is running...
Took 0.519492378999999 seconds.

falcon is running...
Took 0.1276597649999971 seconds.

werkzeug is running...
Took 1.1432917090000032 seconds.

```