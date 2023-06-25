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

Generated on *Sun Jun 25 00:37:58 2023*:

```shell
yrouter is running...
Took 0.22994126700001516 seconds.

django is running...
Took 2.7343935640000154 seconds.

sanic is running...
Took 0.635411471999987 seconds.

falcon is running...
Took 0.15761829800004534 seconds.

werkzeug is running...
Took 1.401028408000002 seconds.

```