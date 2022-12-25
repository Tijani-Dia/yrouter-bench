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

Generated on *Sun Dec 25 00:28:57 2022*:

```shell
yrouter is running...
Took 0.19228037800002085 seconds.

django is running...
Took 2.6846525970000243 seconds.

sanic is running...
Took 0.6186270949999937 seconds.

falcon is running...
Took 0.15444527100001437 seconds.

werkzeug is running...
Took 1.4771381060000124 seconds.

```