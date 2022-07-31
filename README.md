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

Generated on *Sun Jul 31 00:29:55 2022*:

```shell
yrouter is running...
Took 0.1995016759999828 seconds.

django is running...
Took 2.60448161299999 seconds.

sanic is running...
Took 0.634967219999993 seconds.

falcon is running...
Took 0.1561260759999925 seconds.

werkzeug is running...
Took 1.5591946509999843 seconds.

```