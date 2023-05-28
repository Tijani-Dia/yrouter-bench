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

Generated on *Sun May 28 00:29:07 2023*:

```shell
yrouter is running...
Took 0.2131935580000004 seconds.

django is running...
Took 2.9437534429999914 seconds.

sanic is running...
Took 0.6877060099999994 seconds.

falcon is running...
Took 0.1683054529999879 seconds.

werkzeug is running...
Took 1.421709590000006 seconds.

```