from unittest import TestCase
from levelup.character import Character
from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

# class TestCharacterMoveNorthWithinBounds(TestCase):
#     def test_init(self):
#         character = Character("Bad Boy Bobby Blanco")
#         inThisDirection = "N"
#         character.move(inThisDirection)
#         self.assertNotEqual(ENDING_X_POSITION, character.current_position)