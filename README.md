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

Generated on *Sun Oct 29 00:00:54 2023*:

```shell
yrouter is running...
Took 0.22344172399999707 seconds.

django is running...
Took 3.5833869459999903 seconds.

sanic is running...
Took 0.7965572349999945 seconds.

falcon is running...
Took 0.17616290200001572 seconds.

werkzeug is running...
Took 1.7449096340000096 seconds.

```