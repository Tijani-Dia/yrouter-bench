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

Generated on *Sun Mar 12 00:29:59 2023*:

```shell
yrouter is running...
Took 0.2276485579999985 seconds.

django is running...
Took 3.519505548000012 seconds.

sanic is running...
Took 0.8059910930000171 seconds.

falcon is running...
Took 0.19114978100000712 seconds.

werkzeug is running...
Took 2.0631948440000087 seconds.

```