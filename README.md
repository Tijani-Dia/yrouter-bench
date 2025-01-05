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

Generated on *Sun Jan  5 00:00:45 2025*:

```shell
yrouter is running...
Took 0.15201936200000432 seconds.

django is running...
Took 1.968476790000011 seconds.

sanic is running...
Took 0.5190721499999995 seconds.

falcon is running...
Took 0.10298621799998386 seconds.

werkzeug is running...
Took 1.1315903660000117 seconds.

```