from unittest import TestCase
from levelup.position import Position


class TestPositionInitWithXY(TestCase):
    def test_init(self):
        ARBITRARY_X = 5
        ARBITRARY_Y = 0
        testobj = Position(5,0)
        self.assertEqual(ARBITRARY_X, testobj.x)
        self.assertEqual(ARBITRARY_Y, testobj.y)