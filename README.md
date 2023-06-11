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

Generated on *Sun Jun 11 00:33:27 2023*:

```shell
yrouter is running...
Took 0.2599275119999902 seconds.

django is running...
Took 3.7982625789999815 seconds.

sanic is running...
Took 0.8097314990000086 seconds.

falcon is running...
Took 0.20237087499998552 seconds.

werkzeug is running...
Took 1.8583021140000255 seconds.

```