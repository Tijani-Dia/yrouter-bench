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

Generated on *Sun Jun 18 00:33:45 2023*:

```shell
yrouter is running...
Took 0.2312384159999965 seconds.

django is running...
Took 3.110144934999994 seconds.

sanic is running...
Took 0.7154615229999877 seconds.

falcon is running...
Took 0.1839006700000141 seconds.

werkzeug is running...
Took 1.5478659669999786 seconds.

```