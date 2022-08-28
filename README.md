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

Generated on *Sun Aug 28 00:33:46 2022*:

```shell
yrouter is running...
Took 0.19995728499998222 seconds.

django is running...
Took 2.602917985000005 seconds.

sanic is running...
Took 0.6351152999999954 seconds.

falcon is running...
Took 0.16228120499999932 seconds.

werkzeug is running...
Took 1.4630529359999969 seconds.

```