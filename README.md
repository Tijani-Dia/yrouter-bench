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

Generated on *Sun Oct  2 00:44:23 2022*:

```shell
yrouter is running...
Took 0.17100553599999557 seconds.

django is running...
Took 2.4260212830000114 seconds.

sanic is running...
Took 0.5738526239999828 seconds.

falcon is running...
Took 0.13854955499999733 seconds.

werkzeug is running...
Took 1.3407272499999863 seconds.

```