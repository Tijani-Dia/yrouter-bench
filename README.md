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

Generated on *Sun May 14 00:28:29 2023*:

```shell
yrouter is running...
Took 0.19184688100000358 seconds.

django is running...
Took 2.667229481999982 seconds.

sanic is running...
Took 0.638869083000003 seconds.

falcon is running...
Took 0.15877161800000295 seconds.

werkzeug is running...
Took 1.3373277930000143 seconds.

```