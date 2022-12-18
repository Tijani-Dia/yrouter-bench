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

Generated on *Sun Dec 18 00:25:53 2022*:

```shell
yrouter is running...
Took 0.26275771299999917 seconds.

django is running...
Took 3.7380886099999913 seconds.

sanic is running...
Took 0.8297563599999904 seconds.

falcon is running...
Took 0.18484553899999412 seconds.

werkzeug is running...
Took 2.0697912140000057 seconds.

```