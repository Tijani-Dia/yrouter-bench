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

Generated on *Sun Feb  1 00:00:54 2026*:

```shell
yrouter is running...
Took 0.15436740699999518 seconds.

django is running...
Took 2.094904986000003 seconds.

sanic is running...
Took 0.5354469050000006 seconds.

falcon is running...
Took 0.12545184100000029 seconds.

werkzeug is running...
Took 1.1422069450000052 seconds.

```