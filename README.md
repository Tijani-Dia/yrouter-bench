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

Generated on *Sun Aug  7 00:35:11 2022*:

```shell
yrouter is running...
Took 0.19807797999999366 seconds.

django is running...
Took 2.667999344000009 seconds.

sanic is running...
Took 0.6413031529999671 seconds.

falcon is running...
Took 0.16607142499998417 seconds.

werkzeug is running...
Took 1.5250567429999933 seconds.

```