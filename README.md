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

Generated on *Sun Oct 12 00:00:52 2025*:

```shell
yrouter is running...
Took 0.15843376699999823 seconds.

django is running...
Took 2.083630165999999 seconds.

sanic is running...
Took 0.5148156939999993 seconds.

falcon is running...
Took 0.1281697480000048 seconds.

werkzeug is running...
Took 1.1077953489999999 seconds.

```