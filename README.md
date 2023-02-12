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

Generated on *Sun Feb 12 00:31:12 2023*:

```shell
yrouter is running...
Took 0.19957873000001314 seconds.

django is running...
Took 2.612296904999994 seconds.

sanic is running...
Took 0.6328170939999893 seconds.

falcon is running...
Took 0.1571889039999803 seconds.

werkzeug is running...
Took 1.4598617800000113 seconds.

```