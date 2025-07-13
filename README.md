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

Generated on *Sun Jul 13 00:00:54 2025*:

```shell
yrouter is running...
Took 0.15365245799999627 seconds.

django is running...
Took 2.0795172270000037 seconds.

sanic is running...
Took 0.514492740999998 seconds.

falcon is running...
Took 0.10683386699999886 seconds.

werkzeug is running...
Took 1.1281089430000009 seconds.

```