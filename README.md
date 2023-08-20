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

Generated on *Sun Aug 20 00:01:00 2023*:

```shell
yrouter is running...
Took 0.2201475359999847 seconds.

django is running...
Took 3.397565648000011 seconds.

sanic is running...
Took 0.7605891640000095 seconds.

falcon is running...
Took 0.18355628300000149 seconds.

werkzeug is running...
Took 1.6822324439999932 seconds.

```