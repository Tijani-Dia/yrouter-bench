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

Generated on *Sun Mar  5 00:32:54 2023*:

```shell
yrouter is running...
Took 0.1937781839999957 seconds.

django is running...
Took 2.6832246560000215 seconds.

sanic is running...
Took 0.6227215549999983 seconds.

falcon is running...
Took 0.15770524199999159 seconds.

werkzeug is running...
Took 1.5232533389999787 seconds.

```