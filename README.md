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

Generated on *Sun Oct 11 02:20:42 2026*:

```shell
yrouter is running...
Took 0.15535103400000594 seconds.

django is running...
Took 2.0397584920000043 seconds.

sanic is running...
Took 0.5146411279999938 seconds.

falcon is running...
Took 0.12917078499999946 seconds.

werkzeug is running...
Took 1.2713996260000044 seconds.

```