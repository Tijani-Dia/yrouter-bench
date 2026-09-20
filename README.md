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

Generated on *Sun Sep 20 01:47:39 2026*:

```shell
yrouter is running...
Took 0.15489289200002077 seconds.

django is running...
Took 2.0483380689999535 seconds.

sanic is running...
Took 0.5124907829999756 seconds.

falcon is running...
Took 0.12880567399997744 seconds.

werkzeug is running...
Took 1.1532259630000112 seconds.

```