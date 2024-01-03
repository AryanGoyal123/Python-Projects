import unittest
from rect_dataclass import Circle, Rectangle, Square


class TestShapes(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle()
        self.square = Square()
        self.circle = Circle()

    def test_rect_area(self):
        result = self.rectangle.area
        self.assertEqual(result, 0)
