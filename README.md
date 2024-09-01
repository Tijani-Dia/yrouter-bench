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

Generated on *Sun Sep  1 00:00:55 2024*:

```shell
yrouter is running...
Took 0.15447772800001758 seconds.

django is running...
Took 1.901051773000006 seconds.

sanic is running...
Took 0.5096061969999823 seconds.

falcon is running...
Took 0.10265257199998246 seconds.

werkzeug is running...
Took 1.1071901990000015 seconds.

```