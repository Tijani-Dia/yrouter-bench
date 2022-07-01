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

Generated on *Fri Jul  1 15:53:43 2022*:

```shell
yrouter is running...
Took 0.19715151300010803 seconds.

django is running...
Took 2.5823216200001298 seconds.

sanic is running...
Took 0.6537866300000132 seconds.

falcon is running...
Took 0.15483778099996925 seconds.

werkzeug is running...
Took 0.9425689270001385 seconds.

```