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

Generated on *Sun Oct  4 02:56:11 2026*:

```shell
yrouter is running...
Took 0.1524217460000017 seconds.

django is running...
Took 1.7584602350000011 seconds.

sanic is running...
Took 0.4993688439999886 seconds.

falcon is running...
Took 0.12658217899999613 seconds.

werkzeug is running...
Took 1.1590480100000065 seconds.

```