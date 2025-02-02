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

Generated on *Sun Feb  2 00:00:45 2025*:

```shell
yrouter is running...
Took 0.1515060180000205 seconds.

django is running...
Took 2.004774886000007 seconds.

sanic is running...
Took 0.5219334510000238 seconds.

falcon is running...
Took 0.10580096999999 seconds.

werkzeug is running...
Took 1.1229340049999905 seconds.

```