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

Generated on *Sun Apr  2 00:28:36 2023*:

```shell
yrouter is running...
Took 0.2547433510000019 seconds.

django is running...
Took 3.685681598000002 seconds.

sanic is running...
Took 0.7879672029999938 seconds.

falcon is running...
Took 0.19617407500001605 seconds.

werkzeug is running...
Took 1.942466152999998 seconds.

```