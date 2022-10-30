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

Generated on *Sun Oct 30 00:40:01 2022*:

```shell
yrouter is running...
Took 0.22478553700000248 seconds.

django is running...
Took 3.139614817999984 seconds.

sanic is running...
Took 0.7329313799999966 seconds.

falcon is running...
Took 0.1875405600000022 seconds.

werkzeug is running...
Took 1.7710829860000104 seconds.

```