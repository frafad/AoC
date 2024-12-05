import numpy as np
from collections import Counter


def load_data():
    data = np.loadtxt("input.txt", dtype=int)
    return data[:, 0], data[:, 1]


def answer_one(arr1, arr2):
    arr1 = np.sort(arr1)
    arr2 = np.sort(arr2)
    diff = np.abs(arr1 - arr2)
    result = np.sum(diff)
    print("01: ", result)

def answer_two(arr1, arr2):
    c = Counter(arr2)
    sim_scores = np.zeros(shape=(len(arr1),), dtype=int)
    for idx, x in enumerate(arr1):
        sim_scores[idx] = x * c.get(x, 0)
    result = np.sum(sim_scores)
    print("02: ", result)


def main():
    arr1, arr2 = load_data()
    answer_one(arr1, arr2)
    answer_two(arr1, arr2)

if __name__ == "__main__":
    main()