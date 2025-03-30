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

Generated on *Sun Mar 30 00:00:44 2025*:

```shell
yrouter is running...
Took 0.15586673900000392 seconds.

django is running...
Took 1.9777820189999886 seconds.

sanic is running...
Took 0.524152249999986 seconds.

falcon is running...
Took 0.1041743019999899 seconds.

werkzeug is running...
Took 1.1406395479999958 seconds.

```