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

Generated on *Sun Apr 30 00:28:26 2023*:

```shell
yrouter is running...
Took 0.24665758300000107 seconds.

django is running...
Took 3.2654092699999637 seconds.

sanic is running...
Took 0.7371903939999811 seconds.

falcon is running...
Took 0.18610579899996083 seconds.

werkzeug is running...
Took 1.5605513029999543 seconds.

```