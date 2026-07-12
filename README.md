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

Generated on *Sun Jul 12 01:16:06 2026*:

```shell
yrouter is running...
Took 0.15313770299999874 seconds.

django is running...
Took 1.7723152470000016 seconds.

sanic is running...
Took 0.4992468499999987 seconds.

falcon is running...
Took 0.12621400199999755 seconds.

werkzeug is running...
Took 1.070770214999996 seconds.

```