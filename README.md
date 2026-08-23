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

Generated on *Sun Aug 23 00:27:27 2026*:

```shell
yrouter is running...
Took 0.09378554199999911 seconds.

django is running...
Took 1.2122576159999952 seconds.

sanic is running...
Took 0.29985807799999975 seconds.

falcon is running...
Took 0.07529080000000477 seconds.

werkzeug is running...
Took 0.650777644999998 seconds.

```