from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "MyName"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

class TestCharacterMoveNorthWithinBounds(TestCase):
    def test_init(self):
        STARTING_X_POSITION = 0
        STARTING_Y_POSITION = 1
        _from = STARTING_X_POSITION
        _here = STARTING_Y_POSITION
        _toThere = "north"
        character = Character("Bad Boy Billy Blanco")
        character.move(_from, _here, _toThere)
        ENDING_X_POSITION = 0
        ENDING_Y_POSITION = 0
        self.assertEqual(ENDING_X_POSITION, character.xPosition)
        self.assertEqual(ENDING_Y_POSITION, character.yPosition)