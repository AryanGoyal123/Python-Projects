import unittest


class TestPractice(unittest.TestCase):

    def setUp(self):
        pass

    def practice_test_1(self):
        with self.assertRaises(ValueError):
            pass
            # do something to raise the exception

    def practice_test_2(self):
        # do something add call a method
        # result = somefunction()
        # self.assertEqual()
        pass

    # assertEqual(a, b): Asserts that a and b are equal.
    # assertNotEqual(a, b): Asserts that a and b are not equal.

    # assertTrue(x): Asserts that x is True.
    # assertFalse(x): Asserts that x is False.

    # assertIn(a, b): Asserts that a is in the iterable b.
    # assertNotIn(a, b): Asserts that a is not in the iterable b.
