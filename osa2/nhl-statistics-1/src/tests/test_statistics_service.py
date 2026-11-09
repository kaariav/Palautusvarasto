
import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")

    def test_search_does_not_find_player(self):
        player = self.stats.search("Messi")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_team_returns_empty_list(self):
        players = self.stats.team("BOS")
        self.assertEqual(len(players), 0)

    def test_top_returns_players_in_order(self):
        players = self.stats.top(2)

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
