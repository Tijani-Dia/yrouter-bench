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

Generated on *Sun Apr 19 00:06:17 2026*:

```shell
yrouter is running...
Took 0.15112299900000892 seconds.

django is running...
Took 2.0846189089999996 seconds.

sanic is running...
Took 0.5142162039999931 seconds.

falcon is running...
Took 0.1256922940000038 seconds.

werkzeug is running...
Took 1.1383063559999869 seconds.

```