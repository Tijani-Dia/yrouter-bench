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

Generated on *Sun Sep 10 00:00:54 2023*:

```shell
yrouter is running...
Took 0.21423920399999474 seconds.

django is running...
Took 2.788175848999998 seconds.

sanic is running...
Took 0.6573282230000075 seconds.

falcon is running...
Took 0.16564604699999563 seconds.

werkzeug is running...
Took 1.4336064439999916 seconds.

```