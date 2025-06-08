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

Generated on *Sun Jun  8 00:00:52 2025*:

```shell
yrouter is running...
Took 0.15772674400000142 seconds.

django is running...
Took 2.0637575079999806 seconds.

sanic is running...
Took 0.5132592429999931 seconds.

falcon is running...
Took 0.10404944399999749 seconds.

werkzeug is running...
Took 1.1293697349999832 seconds.

```