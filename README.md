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

Generated on *Sun May 21 00:29:23 2023*:

```shell
yrouter is running...
Took 0.19957132599998317 seconds.

django is running...
Took 2.620981069999999 seconds.

sanic is running...
Took 0.6279663229999812 seconds.

falcon is running...
Took 0.1632188650000046 seconds.

werkzeug is running...
Took 1.3115348370000106 seconds.

```