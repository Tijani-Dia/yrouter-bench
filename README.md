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

Generated on *Sun Nov 27 00:30:34 2022*:

```shell
yrouter is running...
Took 0.2269279600000118 seconds.

django is running...
Took 3.100135706000003 seconds.

sanic is running...
Took 0.7358766039999978 seconds.

falcon is running...
Took 0.18977480699999205 seconds.

werkzeug is running...
Took 1.7254197309999881 seconds.

```