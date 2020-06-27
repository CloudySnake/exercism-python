import numpy as np


def triplets_with_sum(number):
    end_range = int(number/2)
    all_triplets = triplets_in_range(end_range, number)
    res = {tuple(sorted(triplet)) for triplet in all_triplets}
    return [list(e) for e in res]


def create_grid(end_range):
    return np.indices((end_range, end_range, 1), dtype=float).reshape(3, -1).T


def triplets_in_range(end_range, number):
    grid = create_grid(end_range)

    grid[:, 2] = (grid[:, 0]**2 + grid[:, 1]**2)**0.5

    grid = grid[(grid[:, 0] + grid[:, 1] + grid[:, 2]) == number]
    grid = grid[(grid[:, 0] != 0) & (grid[:, 1] != 0)]

    return grid.tolist()


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2


if __name__ == "__main__":
    print(triplets_with_sum(30000))
