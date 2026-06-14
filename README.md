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

Generated on *Sun Jun 14 00:21:04 2026*:

```shell
yrouter is running...
Took 0.16016395500000158 seconds.

django is running...
Took 1.7669525000000021 seconds.

sanic is running...
Took 0.49676093299999735 seconds.

falcon is running...
Took 0.12602119499999986 seconds.

werkzeug is running...
Took 1.0603767260000012 seconds.

```