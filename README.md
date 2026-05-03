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

Generated on *Sun May  3 00:11:43 2026*:

```shell
yrouter is running...
Took 0.14746746299999813 seconds.

django is running...
Took 1.7891870440000162 seconds.

sanic is running...
Took 0.47503364199999965 seconds.

falcon is running...
Took 0.11857154399999104 seconds.

werkzeug is running...
Took 0.9937839380000071 seconds.

```