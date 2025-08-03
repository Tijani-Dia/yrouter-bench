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

Generated on *Sun Aug  3 00:01:04 2025*:

```shell
yrouter is running...
Took 0.15369501800000762 seconds.

django is running...
Took 2.057282686999997 seconds.

sanic is running...
Took 0.508899657000029 seconds.

falcon is running...
Took 0.10697604599999977 seconds.

werkzeug is running...
Took 1.1841154799999458 seconds.

```