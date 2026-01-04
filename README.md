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

Generated on *Sun Jan  4 00:00:44 2026*:

```shell
yrouter is running...
Took 0.15615837500001817 seconds.

django is running...
Took 2.258672646999912 seconds.

sanic is running...
Took 0.5174403559999519 seconds.

falcon is running...
Took 0.126377193000053 seconds.

werkzeug is running...
Took 1.1642987699999594 seconds.

```