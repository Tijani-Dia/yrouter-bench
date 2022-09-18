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

Generated on *Sun Sep 18 00:37:10 2022*:

```shell
yrouter is running...
Took 0.19114516600001252 seconds.

django is running...
Took 2.689158329999998 seconds.

sanic is running...
Took 0.6297604760000013 seconds.

falcon is running...
Took 0.15588891999999532 seconds.

werkzeug is running...
Took 1.5091472289999786 seconds.

```