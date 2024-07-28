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

Generated on *Sun Jul 28 00:00:38 2024*:

```shell
yrouter is running...
Took 0.1516351480000253 seconds.

django is running...
Took 1.9700398019999739 seconds.

sanic is running...
Took 0.5130365840000195 seconds.

falcon is running...
Took 0.1028899830000114 seconds.

werkzeug is running...
Took 1.1277395559999945 seconds.

```