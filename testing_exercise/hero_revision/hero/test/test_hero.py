from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def test__init__initializes_correct_values(self):
        player = Hero('Lula', 5, 50, 10)
        self.assertEqual('Lula', player.username)
        self.assertEqual(5, player.level)
        self.assertEqual(50, player.health)
        self.assertEqual(10, player.damage)

    def test__battle__raises_when_players_username_same_as_enemies(self):
        player = Hero('Lula', 5, 50, 10)
        enemy = Hero('Lula', 10, 60, 20)
        with self.assertRaises(Exception) as ex:
            player.battle(enemy)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test__battle__raises_when_players_health_negative_ot_zero(self):
        player = Hero('Lula', 5, 0, 10)
        enemy = Hero('Pepe', 10, 60, 20)
        with self.assertRaises(ValueError) as ex:
            player.battle(enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

        player = Hero('Lula', 5, -10, 10)
        enemy = Hero('Pepe', 10, 60, 20)
        with self.assertRaises(ValueError) as ex:
            player.battle(enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test__battle__raises_when_enemies_health_negative_ot_zero(self):
        player = Hero('Lula', 5, 50, 10)
        enemy = Hero('Pepe', 10, 0, 20)
        with self.assertRaises(ValueError) as ex:
            player.battle(enemy)
        self.assertEqual('You cannot fight Pepe. He needs to rest', str(ex.exception))

        player = Hero('Lula', 5, 50, 10)
        enemy = Hero('Pepe', 10, -10, 20)
        with self.assertRaises(ValueError) as ex:
            player.battle(enemy)
        self.assertEqual('You cannot fight Pepe. He needs to rest', str(ex.exception))

    def test__battle__returns_draw_when_players_and_enemies_health_negative_or_zero(self):
        player = Hero('Lula', 10, 100, 10)
        enemy = Hero('Pepe', 10, 100, 10)

        result = player.battle(enemy)

        self.assertEqual('Draw', result)

        player = Hero('Lula', 100, 100, 10)
        enemy = Hero('Pepe', 100, 100, 10)

        result = player.battle(enemy)

        self.assertEqual('Draw', result)

    def test__battle__increases_players_stats_and_returns_win_message_when_enemy_defeated(self):
        player = Hero('Lula', 100, 1000, 10)  # 1000
        enemy = Hero('Pepe', 10, 100, 10)  # 100

        result = player.battle(enemy)

        self.assertEqual(101, player.level)
        self.assertEqual(905, player.health)
        self.assertEqual(15, player.damage)
        self.assertEqual('You win', result)

    def test__battle__increases_enemies_stats_and_returns_loss_message_when_player_defeated(self):
        player = Hero('Lula', 10, 100, 10)  # 100
        enemy = Hero('Pepe', 100, 1000, 10)  # 1000

        result = player.battle(enemy)

        self.assertEqual(101, enemy.level)
        self.assertEqual(905, enemy.health)
        self.assertEqual(15, enemy.damage)
        self.assertEqual('You lose', result)

    def test__str__returns_correct_message(self):
        player = Hero('Lula', 10, 100, 5)
        result = player.__str__()
        self.assertEqual(f"Hero Lula: 10 lvl\n"
                         f"Health: 100\n"
                         f"Damage: 5\n", result)


if __name__ == "__main__":
    main()
