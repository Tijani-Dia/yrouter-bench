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

Generated on *Sun Jul  9 00:01:02 2023*:

```shell
yrouter is running...
Took 0.2041930759999957 seconds.

django is running...
Took 2.815491585999993 seconds.

sanic is running...
Took 0.6561407100000025 seconds.

falcon is running...
Took 0.1688934990000064 seconds.

werkzeug is running...
Took 1.4272682779999997 seconds.

```