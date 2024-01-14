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

Generated on *Sun Jan 14 00:00:45 2024*:

```shell
yrouter is running...
Took 0.16408484800001588 seconds.

django is running...
Took 2.1231808840000213 seconds.

sanic is running...
Took 0.518724021999958 seconds.

falcon is running...
Took 0.10187019199997849 seconds.

werkzeug is running...
Took 1.131403874 seconds.

```