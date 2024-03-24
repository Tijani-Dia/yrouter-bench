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

Generated on *Sun Mar 24 00:00:37 2024*:

```shell
yrouter is running...
Took 0.1612916880000057 seconds.

django is running...
Took 2.1256266499999867 seconds.

sanic is running...
Took 0.5471989720000181 seconds.

falcon is running...
Took 0.10114837999998372 seconds.

werkzeug is running...
Took 1.1898624279999979 seconds.

```