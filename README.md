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

Generated on *Sun Aug 30 01:50:34 2026*:

```shell
yrouter is running...
Took 0.10485960799999816 seconds.

django is running...
Took 1.3535315670000045 seconds.

sanic is running...
Took 0.3259302780000013 seconds.

falcon is running...
Took 0.09017132399999639 seconds.

werkzeug is running...
Took 0.6449029879999983 seconds.

```