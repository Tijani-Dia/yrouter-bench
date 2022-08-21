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

Generated on *Sun Aug 21 00:28:32 2022*:

```shell
yrouter is running...
Took 0.19339105299999915 seconds.

django is running...
Took 2.7102899549999933 seconds.

sanic is running...
Took 0.6445261269999918 seconds.

falcon is running...
Took 0.15805681300000174 seconds.

werkzeug is running...
Took 1.5397109590000042 seconds.

```