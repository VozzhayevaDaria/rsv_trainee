import unittest
from figure import Circle
from figure import Triangle
from math import pi

class Test(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle([0, 0, 0])
        self.circle = Circle([0])

    def test_basic_triangle(self):
        self.assertEqual(self.triangle.set_params([5, 5, 6]).area(), 12)
        self.assertEqual(self.triangle.set_params([5, 5, 8]).area(), 12)

    def test_degenerate_triangle(self):
        err = "Warn: the figure can't be triangle"
        self.assertEqual(self.triangle.set_params([3, 4, 8]).area(), err)
        self.assertEqual(self.triangle.set_params([7, 2, 4]).area(), err)
        self.assertEqual(self.triangle.set_params([1, 6, 4]).area(), err)

    def test_rectangle_triangle(self):
        self.assertEqual(self.triangle.set_params([3, 4, 5]).rect_check(), True)
        self.assertEqual(self.triangle.set_params([3, 5, 5]).rect_check(), False)

    def test_basic_circle(self):
        self.assertEqual(self.circle.set_params([1]).area(), pi)
        self.assertEqual(self.circle.set_params([2]).area(), pi * 4)
        self.assertEqual(self.circle.set_params([3]).area(), pi * 9)

    def test_degenerate_circle(self):
        err = "Warn: the figure can't be circle"
        self.assertEqual(self.circle.set_params([0]).area(), err)
        self.assertEqual(self.circle.set_params([-1]).area(), err)
        self.assertEqual(self.circle.set_params([-2]).area(), err)

if __name__ == "__main__":
  unittest.main()