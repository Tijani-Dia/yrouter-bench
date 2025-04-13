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

Generated on *Sun Apr 13 00:24:30 2025*:

```shell
yrouter is running...
Took 0.15575278599999365 seconds.

django is running...
Took 2.018035376000057 seconds.

sanic is running...
Took 0.5299838930000078 seconds.

falcon is running...
Took 0.10455277100004423 seconds.

werkzeug is running...
Took 1.1289801159999797 seconds.

```