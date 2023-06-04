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

Generated on *Sun Jun  4 00:35:08 2023*:

```shell
yrouter is running...
Took 0.22118081899998288 seconds.

django is running...
Took 2.9380645649999906 seconds.

sanic is running...
Took 0.6626547469999764 seconds.

falcon is running...
Took 0.1816727699999774 seconds.

werkzeug is running...
Took 1.5048697400000037 seconds.

```