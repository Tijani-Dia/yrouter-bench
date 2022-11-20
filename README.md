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

Generated on *Sun Nov 20 00:33:21 2022*:

```shell
yrouter is running...
Took 0.2090595800000017 seconds.

django is running...
Took 2.68902264099998 seconds.

sanic is running...
Took 0.6452424040000153 seconds.

falcon is running...
Took 0.15688208199998144 seconds.

werkzeug is running...
Took 1.5028761499999916 seconds.

```