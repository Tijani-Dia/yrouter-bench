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

Generated on *Sun Jul 30 00:01:16 2023*:

```shell
yrouter is running...
Took 0.26304867100000706 seconds.

django is running...
Took 3.9497615109999913 seconds.

sanic is running...
Took 0.8976459810000108 seconds.

falcon is running...
Took 0.20517014199998584 seconds.

werkzeug is running...
Took 1.9341543300000126 seconds.

```