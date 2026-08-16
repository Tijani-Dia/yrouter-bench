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

Generated on *Sun Aug 16 00:26:35 2026*:

```shell
yrouter is running...
Took 0.1522257410000094 seconds.

django is running...
Took 1.7816797109999953 seconds.

sanic is running...
Took 0.4940338159999982 seconds.

falcon is running...
Took 0.12586901500000636 seconds.

werkzeug is running...
Took 1.0526654110000067 seconds.

```