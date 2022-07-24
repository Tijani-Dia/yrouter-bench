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

Generated on *Sun Jul 24 00:33:46 2022*:

```shell
yrouter is running...
Took 0.2012034969999945 seconds.

django is running...
Took 2.5506597860000397 seconds.

sanic is running...
Took 0.6543641960000173 seconds.

falcon is running...
Took 0.15984435199999325 seconds.

werkzeug is running...
Took 1.4795119080000063 seconds.

```