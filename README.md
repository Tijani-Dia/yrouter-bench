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

Generated on *Sun Dec  4 00:26:11 2022*:

```shell
yrouter is running...
Took 0.19211937699999737 seconds.

django is running...
Took 2.6792372370000095 seconds.

sanic is running...
Took 0.6494828860000013 seconds.

falcon is running...
Took 0.1558598440000054 seconds.

werkzeug is running...
Took 1.5167130410000027 seconds.

```