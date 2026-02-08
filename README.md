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

Generated on *Sun Feb  8 00:04:05 2026*:

```shell
yrouter is running...
Took 0.14796492499999658 seconds.

django is running...
Took 1.8085052229999974 seconds.

sanic is running...
Took 0.47919682199994895 seconds.

falcon is running...
Took 0.12287876499999584 seconds.

werkzeug is running...
Took 0.9930942319999758 seconds.

```