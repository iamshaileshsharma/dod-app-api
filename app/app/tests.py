from django.test import TestCase

from app.calc import add, subtract


class ClacTests(TestCase):
    def test_add_number(self):
        """ Two number addition """
        self.assertEqual(add(3,8),11)

    def test_subtract_number(self):
        """ Test that value subtract and return """
        self.assertEqual(subtract(8,3), 5)
