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

Generated on *Sun May 31 00:18:19 2026*:

```shell
yrouter is running...
Took 0.1636949960000038 seconds.

django is running...
Took 2.092055485000003 seconds.

sanic is running...
Took 0.5140057229999968 seconds.

falcon is running...
Took 0.12754748400001858 seconds.

werkzeug is running...
Took 1.161371717999998 seconds.

```