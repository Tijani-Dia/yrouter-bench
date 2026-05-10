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

Generated on *Sun May 10 00:13:25 2026*:

```shell
yrouter is running...
Took 0.15320838200000253 seconds.

django is running...
Took 1.7611859630000026 seconds.

sanic is running...
Took 0.5208915970000021 seconds.

falcon is running...
Took 0.13004550900001277 seconds.

werkzeug is running...
Took 1.054974088000023 seconds.

```