class FootballTeam:

    def __init__(self, team_name: str, coach: str):
        self.tema_name = team_name
        self.coach = coach
        self.players = []

    def add_player(
        self,
        name: str,
        position: str,
        number: int,
        age: int,
        nationality: str
    ):
        self.players.append({
                "name": name,
                "position": position,
                "number": number,
                "age": age,
                "nationality": nationality
            })

    def remove_player(self, number: int):
        for player in self.players:
            if player["number"] == number:
                self.players.remove(player)
                return f"player {number} removed"
        else:
            return f"player {number} not found"

    def edit_player(self, number: int, **kwargs):
        for player in self.players:
            if player["number"] == number:
                player.update(kwargs)
                return f"player {number} info updated"
        else:
            return f"player {number} not found"

    def team_info(self):
        return f"team {self.tema_name}, coach {self.coach} players {self.players}"

    def player_info(self, number: int):
        for player in self.players:
            if player["number"] == number:
                return player
        else:
            return f"player {number} not found"
