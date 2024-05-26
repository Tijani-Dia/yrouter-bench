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

Generated on *Sun May 26 00:00:36 2024*:

```shell
yrouter is running...
Took 0.16465162899999086 seconds.

django is running...
Took 2.022377801999994 seconds.

sanic is running...
Took 0.507118848999994 seconds.

falcon is running...
Took 0.10445400200001131 seconds.

werkzeug is running...
Took 1.1247568510000008 seconds.

```