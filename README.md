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

Generated on *Sun Aug 17 00:00:57 2025*:

```shell
yrouter is running...
Took 0.15441312399997287 seconds.

django is running...
Took 2.1903769780000175 seconds.

sanic is running...
Took 0.5135355130000221 seconds.

falcon is running...
Took 0.12792894199998273 seconds.

werkzeug is running...
Took 1.1343927799999847 seconds.

```