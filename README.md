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

Generated on *Sun Sep  3 00:00:50 2023*:

```shell
yrouter is running...
Took 0.20539440000001719 seconds.

django is running...
Took 2.7960346979999997 seconds.

sanic is running...
Took 0.6559609490000184 seconds.

falcon is running...
Took 0.16893897599999264 seconds.

werkzeug is running...
Took 1.4333362829999885 seconds.

```