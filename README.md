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

Generated on *Sun Aug 24 00:00:53 2025*:

```shell
yrouter is running...
Took 0.15340554200000156 seconds.

django is running...
Took 2.1942286519999925 seconds.

sanic is running...
Took 0.5170806300000095 seconds.

falcon is running...
Took 0.12696573700003455 seconds.

werkzeug is running...
Took 1.136551752999992 seconds.

```