import numpy as np


def load_data():
    """
    Reads a file and loads its contents into a list of lists of integers.
    """
    with open("/home/frafad/code/AoC/2024/02/input.txt", "r") as f:
        data = [list(map(int, line.split())) for line in f]
    return data

def main():
    data = load_data()
    result = []
    for report in data:
        for i in range(len(report) - 1):
            report[i] = report[i+1] - report[i]
        report = report[:-1]
        if all(n>0 for n in report) or all(n<0 for n in report):
            report = [abs(n) for n in report]
            report = 1 if all(n>=1 and n<=3 for n in report) else 0
        else:
            report = 0
        result.append(report)
    print(result)
    print(sum(result))

if __name__ == "__main__":
    main()