from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def test_valid_initialization_operation(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.assertEqual(self.player.name, 'ABC')
        self.assertEqual(self.player.age, 19)
        self.assertEqual(self.player.points, 1.0)
        self.assertFalse(self.player.wins)

    def test_invalid_name_len_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('AB', 19, 1.0)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_invalid_age_under_18_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('ABC', 17, 1.0)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_unsuccessful_add_win_already_existing(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.player.add_new_win('aaa')
        self.assertIn('aaa', self.player.wins)
        result = self.player.add_new_win('aaa')
        self.assertEqual(result, "aaa has been already added to the list of wins!")

    def test_successful_add_win_operation(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.player.add_new_win('aaa')
        self.assertIn('aaa', self.player.wins)

    def test_successful__lt__operation(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.other_player = TennisPlayer('CBA', 19, 1.1)
        result = self.player < self.other_player
        self.assertEqual(result, f'CBA is a top seeded player and he/she is better than ABC')

    def test_successful__lt__operation_reverse(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.other_player = TennisPlayer('CBA', 19, 1.1)
        result = self.player > self.other_player
        self.assertEqual(result, f'CBA is a better player than ABC')

    def test_successful__lt__operation_equal(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.other_player = TennisPlayer('CBA', 19, 1.0)
        result = self.player > self.other_player
        self.assertEqual('CBA is a better player than ABC', result)

    def test_successful__str__operation(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.assertEqual(str(self.player), 'Tennis Player: ABC\nAge: 19\nPoints: 1.0\nTournaments won: ')

    def test_successful__str__operation_with_win(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.player.add_new_win('a')
        self.assertEqual(str(self.player), 'Tennis Player: ABC\nAge: 19\nPoints: 1.0\nTournaments won: a')

    def test_successful__str__operation_with_more_win(self):
        self.player = TennisPlayer('ABC', 19, 1.0)
        self.player.add_new_win('a')
        self.player.add_new_win('b')
        self.player.add_new_win('c')
        self.assertEqual(str(self.player), 'Tennis Player: ABC\nAge: 19\nPoints: 1.0\nTournaments won: a, b, c')


if __name__ == '__main__':
    main()
