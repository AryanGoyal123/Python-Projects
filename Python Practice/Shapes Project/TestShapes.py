import unittest
from rect_dataclass import Circle, Rectangle, Square


class TestShapes(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle()
        self.square = Square()
        self.circle = Circle()

    def test_width_setter_with_non_positive_value(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -5  # This should raise a ValueError

    def test_height_setter_with_non_positive_value(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = -5  # This should raise a ValueError

    def test_side_setter_with_non_positive_value(self):
        with self.assertRaises(ValueError):
            self.square.width = -5  # This should raise a ValueError

    def test_rect_area_pos(self):
        self.rectangle.height = 2
        self.rectangle.width = 2
        result = self.rectangle.area
        self.assertEqual(result, 4)

    def test_rect_perimeter_pos(self):
        self.rectangle.height = 3
        self.rectangle.width = 3
        result = self.rectangle.perimeter
        self.assertEqual(result, 12)

    def test_diameter_setter_with_non_positive_value(self):
        with (self.assertRaises(ValueError)):
            self.circle.diameter = -5  # This should raise a ValueError
