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

Generated on *Sun Sep 13 01:31:03 2026*:

```shell
yrouter is running...
Took 0.12057626999998661 seconds.

django is running...
Took 1.3467262819999917 seconds.

sanic is running...
Took 0.38719577300000196 seconds.

falcon is running...
Took 0.09887449100000367 seconds.

werkzeug is running...
Took 0.8319131719999859 seconds.

```