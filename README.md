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

Generated on *Sun Oct 23 00:42:59 2022*:

```shell
yrouter is running...
Took 0.24152635100000452 seconds.

django is running...
Took 3.7131964290000212 seconds.

sanic is running...
Took 0.7994339040000114 seconds.

falcon is running...
Took 0.2067688159999932 seconds.

werkzeug is running...
Took 2.011647609000022 seconds.

```