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

Generated on *Sun Jul 19 01:14:25 2026*:

```shell
yrouter is running...
Took 0.1528231859999991 seconds.

django is running...
Took 1.7598340799999974 seconds.

sanic is running...
Took 0.5054723709999962 seconds.

falcon is running...
Took 0.1269719330000001 seconds.

werkzeug is running...
Took 1.0575858360000012 seconds.

```