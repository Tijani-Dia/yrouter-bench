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

Generated on *Sun Jul  3 00:30:12 2022*:

```shell
yrouter is running...
Took 0.17296040400000834 seconds.

django is running...
Took 2.2467080349999975 seconds.

sanic is running...
Took 0.5803517330000005 seconds.

falcon is running...
Took 0.13576991100001123 seconds.

werkzeug is running...
Took 0.8903213809999926 seconds.

```