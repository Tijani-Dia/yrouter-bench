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

Generated on *Sun Sep 11 00:31:42 2022*:

```shell
yrouter is running...
Took 0.19564130999998497 seconds.

django is running...
Took 2.5986008510000147 seconds.

sanic is running...
Took 0.6509436830000084 seconds.

falcon is running...
Took 0.1653431619999992 seconds.

werkzeug is running...
Took 1.479452545000015 seconds.

```