import subprocess
from datetime import datetime


def generate_readme():
    bench_results = subprocess.run(
        ["python3", "bench.py"], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    with open("README.txt") as f:
        base_readme = f.read()

    with open("README.md", "w") as readme:
        readme.write(base_readme)
        readme.write(f"Generated on *{datetime.now().ctime()}*:\n\n")
        readme.write(f"```shell\n{bench_results}```")


if __name__ == "__main__":
    generate_readme()
