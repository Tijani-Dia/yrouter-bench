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

Generated on *Sun Jul 26 01:20:20 2026*:

```shell
yrouter is running...
Took 0.09332054300000436 seconds.

django is running...
Took 1.1818682859999967 seconds.

sanic is running...
Took 0.29207594400000403 seconds.

falcon is running...
Took 0.0744590950000088 seconds.

werkzeug is running...
Took 0.6360564490000087 seconds.

```