import unittest
from unittest.mock import patch
from player_character import PlayerCharacter


class TestPlayerCharacter(unittest.TestCase):
    def setUp(self):
        self.player = PlayerCharacter("Alex", 25)

    def test_membership(self):
        self.assertEqual(self.player.membership, True)

    def test_name_attribute(self):
        self.assertEqual(self.player.name, "Alex")

    def test_age_attribute(self):
        self.assertEqual(self.player.age, 25)

    def test_shout_method(self):
        with patch("builtins.print") as mocked_print:
            self.player.shout()
            mocked_print.assert_called_with("My name is Alex")

    def test_adding_things_class_method(self):
        new_player = PlayerCharacter.adding_things(2, 3)
        self.assertEqual(new_player.name, "Teddy")
        self.assertEqual(new_player.age, 5)

    def test_adding_things2_static_method(self):
        result = PlayerCharacter.adding_things2(2, 3)
        self.assertEqual(result, 5)
