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

Generated on *Sun Sep  6 01:25:01 2026*:

```shell
yrouter is running...
Took 0.15671843600011925 seconds.

django is running...
Took 2.127714069000149 seconds.

sanic is running...
Took 0.517533966999963 seconds.

falcon is running...
Took 0.12598929899991163 seconds.

werkzeug is running...
Took 1.1744854860000942 seconds.

```