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

Generated on *Sun Mar 31 00:00:40 2024*:

```shell
yrouter is running...
Took 0.15716803499998377 seconds.

django is running...
Took 1.9851622129999953 seconds.

sanic is running...
Took 0.5196069020000209 seconds.

falcon is running...
Took 0.10332839599999488 seconds.

werkzeug is running...
Took 1.1325466449999908 seconds.

```