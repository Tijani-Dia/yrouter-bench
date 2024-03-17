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

Generated on *Sun Mar 17 00:00:41 2024*:

```shell
yrouter is running...
Took 0.16991528100001574 seconds.

django is running...
Took 2.139275475000005 seconds.

sanic is running...
Took 0.5173670759999993 seconds.

falcon is running...
Took 0.10380322599999658 seconds.

werkzeug is running...
Took 1.125971934000006 seconds.

```