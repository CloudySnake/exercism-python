import unittest

from pythagorean_triplet import triplets_with_sum, is_triplet, triplets_in_range

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, "assertCountEqual"):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class PythagoreanTripletTest(unittest.TestCase):
    def test_triplets_whose_sum_is_12(self):
        self.assertCountEqual(triplets_with_sum(12), [[3, 4, 5]])

    def test_triplets_whose_sum_is_108(self):
        self.assertCountEqual(triplets_with_sum(108), [[27, 36, 45]])

    def test_triplets_whose_sum_is_1000(self):
        self.assertCountEqual(triplets_with_sum(1000), [[200, 375, 425]])

    def test_no_matching_triplets_for_1001(self):
        self.assertCountEqual(triplets_with_sum(1001), [])

    def test_returns_all_matching_triplets(self):
        self.assertCountEqual(triplets_with_sum(90), [[9, 40, 41], [15, 36, 39]])

    def test_several_matching_triplets(self):
        self.assertEqual(
            len(triplets_with_sum(840)),
            len([
                [40, 399, 401],
                [56, 390, 394],
                [105, 360, 375],
                [120, 350, 370],
                [140, 336, 364],
                [168, 315, 357],
                [210, 280, 350],
                [240, 252, 348],
            ]),
        )
        self.assertCountEqual(
            triplets_with_sum(840),
            [
                [40, 399, 401],
                [56, 390, 394],
                [105, 360, 375],
                [120, 350, 370],
                [140, 336, 364],
                [168, 315, 357],
                [210, 280, 350],
                [240, 252, 348],
            ],
        )

    def test_triplets_for_medium_number(self):
        self.assertCountEqual(
            triplets_with_sum(3_000),
            [
                [750, 1000, 1250.0], [600, 1125, 1275.0], [500, 1200, 1300.0]
            ]
        )

    # def test_triplets_for_large_number(self):
    #     triplets = triplets_with_sum(30_000)
    #     expected = [
    #             [1200, 14375, 14425],
    #             [1875, 14000, 14125],
    #             [5000, 12000, 13000],
    #             [6000, 11250, 12750],
    #             [7500, 10000, 12500],
    #         ]
    #     self.assertEqual(len(triplets), len(expected))
    #     self.assertCountEqual(triplets, expected)


class TestIsTriplet:
    def test_valid_triplet(self):
        triplet = [3, 4, 5]
        assert is_triplet(triplet) is True

    def test_valid_triplet_unordered(self):
        triplet = [4, 3, 5]
        assert is_triplet(triplet) is True

    def test_invalid_triplet(self):
        triplet = [2, 4, 5]
        assert is_triplet(triplet) is False


# class TestTripletsInRange:
#     def test_small_range(self):
#         assert triplets_in_range(1, 13) == [[3, 4, 5]]


if __name__ == "__main__":
    unittest.main()
