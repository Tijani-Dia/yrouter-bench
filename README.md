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

Generated on *Sun Sep  7 00:00:51 2025*:

```shell
yrouter is running...
Took 0.15264368899988767 seconds.

django is running...
Took 2.0866109129999586 seconds.

sanic is running...
Took 0.5085119089999353 seconds.

falcon is running...
Took 0.12863411400007863 seconds.

werkzeug is running...
Took 1.123865983000087 seconds.

```