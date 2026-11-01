import unittest
from unittest.mock import Mock

from hangman import play_game


class HangmanTests(unittest.TestCase):
    def test_player_can_win(self):
        guesses = iter(["x", "p", "y", "t", "h", "o", "n"])
        output = Mock()
        self.assertTrue(play_game("python", lambda _: next(guesses), output))
        self.assertTrue(any("You won" in call.args[0] for call in output.call_args_list))

    def test_player_loses_after_six_wrong_guesses(self):
        guesses = iter(["a", "b", "c", "d", "e", "f"])
        self.assertFalse(play_game("python", lambda _: next(guesses), lambda _: None))


if __name__ == "__main__":
    unittest.main()
