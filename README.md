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

Generated on *Sun Jun 16 00:00:42 2024*:

```shell
yrouter is running...
Took 0.1546699330000081 seconds.

django is running...
Took 2.021394454000017 seconds.

sanic is running...
Took 0.5117775719999713 seconds.

falcon is running...
Took 0.10167253299999857 seconds.

werkzeug is running...
Took 1.116108865000001 seconds.

```