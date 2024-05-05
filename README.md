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

Generated on *Sun May  5 00:01:10 2024*:

```shell
yrouter is running...
Took 0.15280932300001382 seconds.

django is running...
Took 1.983647459000025 seconds.

sanic is running...
Took 0.5233885270000087 seconds.

falcon is running...
Took 0.10461424700000066 seconds.

werkzeug is running...
Took 1.123578961999982 seconds.

```