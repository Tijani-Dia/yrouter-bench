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

Generated on *Sun Sep 22 00:00:50 2024*:

```shell
yrouter is running...
Took 0.1551624810000476 seconds.

django is running...
Took 1.986917687000016 seconds.

sanic is running...
Took 0.5257009150000158 seconds.

falcon is running...
Took 0.101098904999958 seconds.

werkzeug is running...
Took 1.1320993069999759 seconds.

```