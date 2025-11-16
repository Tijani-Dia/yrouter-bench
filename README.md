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

Generated on *Sun Nov 16 00:00:48 2025*:

```shell
yrouter is running...
Took 0.16498159600000406 seconds.

django is running...
Took 2.0925892180000005 seconds.

sanic is running...
Took 0.5080929089999984 seconds.

falcon is running...
Took 0.1255002970000021 seconds.

werkzeug is running...
Took 1.1296424889999983 seconds.

```