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

Generated on *Sun Mar 15 00:02:45 2026*:

```shell
yrouter is running...
Took 0.15695876500001305 seconds.

django is running...
Took 2.070938837999961 seconds.

sanic is running...
Took 0.5156554199999732 seconds.

falcon is running...
Took 0.12520076800001334 seconds.

werkzeug is running...
Took 1.1394554190000008 seconds.

```