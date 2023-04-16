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

Generated on *Sun Apr 16 00:27:09 2023*:

```shell
yrouter is running...
Took 0.1911819249999951 seconds.

django is running...
Took 2.7130281580000144 seconds.

sanic is running...
Took 0.6233426080000015 seconds.

falcon is running...
Took 0.1552631889999816 seconds.

werkzeug is running...
Took 1.4939081709999869 seconds.

```