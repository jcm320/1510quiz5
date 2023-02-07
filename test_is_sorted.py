from unittest import TestCase
from sort_list import is_sorted

class TestIsSorted(TestCase):
    def test_is_sorted(self):
        self.assertEqual(True, is_sorted([1,2,3]))
        self.assertEqual(False, is_sorted([4,3,2]))
        self.assertEqual(False, is_sorted([-3,-5,7]))
        self.assertEqual(True, is_sorted([-7,-4,-3,0,3,4,5]))
        self.assertEqual(True, is_sorted([]))
