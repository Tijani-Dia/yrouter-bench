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

Generated on *Sun Jul 10 00:33:59 2022*:

```shell
yrouter is running...
Took 0.19787354600001095 seconds.

django is running...
Took 2.587987635000019 seconds.

sanic is running...
Took 0.6505458400000066 seconds.

falcon is running...
Took 0.15224404299999605 seconds.

werkzeug is running...
Took 0.9485363699999994 seconds.

```