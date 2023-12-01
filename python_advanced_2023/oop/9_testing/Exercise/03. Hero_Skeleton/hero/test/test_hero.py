from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.test_hero = Hero('Roland', 60, 3200, 250)

    def test_successful_init_operation(self):
        self.assertEqual(self.test_hero.username, 'Roland')
        self.assertEqual(self.test_hero.level, 60)
        self.assertEqual(self.test_hero.health, 3200)
        self.assertEqual(self.test_hero.damage, 250)

    def test_unsuccessful_battle_raise_exception(self):
        enemy = Hero('Roland', 1, 100, 15)
        with self.assertRaises(Exception) as ex:
            self.test_hero.battle(enemy)
        self.assertEqual(str(ex.exception), 'You cannot fight yourself')

    def test_unsuccessful_battle_low_hp_raise_ve(self):
        enemy = Hero('LowlyRat', 5, 50, 10)
        self.test_hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(enemy)
        self.assertFalse(self.test_hero.health)
        self.assertEqual(str(ve.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_unsuccessful_battle_enemy_low_hp_raise_ve(self):
        enemy = Hero('LowlyRat', 5, 50, 10)
        self.assertTrue(enemy.health > 0)
        enemy.health = 0
        self.assertFalse(enemy.health)
        with self.assertRaises(ValueError) as ve:
            self.test_hero.battle(enemy)
        self.assertEqual(str(ve.exception), f'You cannot fight {enemy.username}. He needs to rest')

    def test_successful_battle_draw_operation(self):
        enemy = Hero('LowlyRat', 60, 3200, 250)
        result = self.test_hero.battle(enemy)
        self.assertEqual(self.test_hero.health, enemy.health)
        self.assertEqual(result, 'Draw')
        self.assertTrue(self.test_hero.health <= 0)
        self.assertTrue(enemy.health <= 0)

    def test_successful_battle_win_operation(self):
        enemy = Hero('LowlyRat', 5, 50, 10)
        result = self.test_hero.battle(enemy)
        self.assertEqual(result, 'You win')
        self.assertTrue(self.test_hero.health > 0)
        self.assertTrue(self.test_hero.level > 60)
        self.assertTrue(self.test_hero.health == 3155)
        self.assertTrue(enemy.health <= 0)

    def test_successful_battle_lose_operation(self):
        enemy = Hero('KingRat', 60, 16000, 450)
        result = self.test_hero.battle(enemy)
        self.assertEqual(result, 'You lose')
        self.assertTrue(enemy.level == 61)
        self.assertTrue(enemy.damage == 455)
        self.assertTrue(enemy.health == 1005)

    def test_successful__str__operation(self):
        result = f'Hero Roland: 60 lvl\nHealth: 3200\nDamage: 250\n'
        self.assertEqual(result, str(self.test_hero))


if __name__ == '__main__':
    main()
