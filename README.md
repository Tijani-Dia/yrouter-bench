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

Generated on *Sun Mar 26 00:29:32 2023*:

```shell
yrouter is running...
Took 0.20053384400000596 seconds.

django is running...
Took 2.5999351399999853 seconds.

sanic is running...
Took 0.6302084379999826 seconds.

falcon is running...
Took 0.15901436900000476 seconds.

werkzeug is running...
Took 1.4753876710000213 seconds.

```