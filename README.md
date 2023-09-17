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

Generated on *Sun Sep 17 00:01:10 2023*:

```shell
yrouter is running...
Took 0.22291679799999997 seconds.

django is running...
Took 3.5474655190000135 seconds.

sanic is running...
Took 0.734888073999997 seconds.

falcon is running...
Took 0.1799817419999954 seconds.

werkzeug is running...
Took 1.7079710379999824 seconds.

```