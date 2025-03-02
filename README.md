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

Generated on *Sun Mar  2 00:00:37 2025*:

```shell
yrouter is running...
Took 0.15463512500001286 seconds.

django is running...
Took 1.9672799439999977 seconds.

sanic is running...
Took 0.5261011400000086 seconds.

falcon is running...
Took 0.10284155899998382 seconds.

werkzeug is running...
Took 1.1284045369999944 seconds.

```