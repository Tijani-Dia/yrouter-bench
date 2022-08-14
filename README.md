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

Generated on *Sun Aug 14 00:31:26 2022*:

```shell
yrouter is running...
Took 0.20016586500003086 seconds.

django is running...
Took 2.7023227779999957 seconds.

sanic is running...
Took 0.6399457019999772 seconds.

falcon is running...
Took 0.15548850400000447 seconds.

werkzeug is running...
Took 1.5150375300000292 seconds.

```