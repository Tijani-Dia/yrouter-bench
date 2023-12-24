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

Generated on *Sun Dec 24 00:00:45 2023*:

```shell
yrouter is running...
Took 0.15156597800000782 seconds.

django is running...
Took 2.157436964999988 seconds.

sanic is running...
Took 0.524904800999991 seconds.

falcon is running...
Took 0.10123409400000583 seconds.

werkzeug is running...
Took 1.1074211700000092 seconds.

```