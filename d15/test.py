import unittest

from .main import FootballTeam  # adjust import path as needed


class TestFootballTeam(unittest.TestCase):

    def setUp(self):
        self.team = FootballTeam("Arsenal", "Arteta")
        self.team.add_player("Saka", "RW", 7, 23, "England")
        self.team.add_player("Ødegaard", "CAM", 8, 25, "Norway")

    def test_add_player(self):
        self.team.add_player("Rice", "CDM", 41, 26, "England")
        self.assertEqual(len(self.team.players), 3)
        self.assertEqual(self.team.players[-1]["name"], "Rice")

    def test_remove_player_exists(self):
        result = self.team.remove_player(7)
        self.assertEqual(result, "player 7 removed")
        self.assertEqual(len(self.team.players), 1)

    def test_remove_player_not_exists(self):
        result = self.team.remove_player(99)
        self.assertEqual(result, "player 99 not found")
        self.assertEqual(len(self.team.players), 2)

    def test_edit_player_exists(self):
        result = self.team.edit_player(8, age=26, nationality="Norwegian")
        self.assertEqual(result, "player 8 info updated")
        player = self.team.player_info(8)
        self.assertEqual(player["age"], 26)
        self.assertEqual(player["nationality"], "Norwegian")

    def test_edit_player_not_exists(self):
        result = self.team.edit_player(99, name="Unknown")
        self.assertEqual(result, "player 99 not found")

    def test_team_info(self):
        info = self.team.team_info()
        self.assertIn("Arsenal", info)
        self.assertIn("Arteta", info)
        self.assertIn("Saka", info)

    def test_player_info_exists(self):
        player = self.team.player_info(8)
        self.assertEqual(player["name"], "Ødegaard")

    def test_player_info_not_exists(self):
        result = self.team.player_info(99)
        self.assertEqual(result, "player 99 not found")


if __name__ == "__main__":
    unittest.main()
