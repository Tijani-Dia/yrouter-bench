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

Generated on *Sun Nov 30 00:00:49 2025*:

```shell
yrouter is running...
Took 0.15470492500000432 seconds.

django is running...
Took 2.112880789000002 seconds.

sanic is running...
Took 0.5069258910000087 seconds.

falcon is running...
Took 0.12537651600000288 seconds.

werkzeug is running...
Took 1.1339920040000067 seconds.

```