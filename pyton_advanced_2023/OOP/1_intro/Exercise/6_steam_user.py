class SteamUser:
    def __init__(self, username: str, games: list):
        self.username = username
        self.games = list(games)
        self.played_hours = 0

    def play(self, game_name: int, hours: int):
        if game_name in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game_name}'
        return f'{game_name} is not in library'

    def buy_game(self, game: str):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'


user = SteamUser("Me", ["CSGO", "Like A Dragon"])
print(user.play("CSGO", 3))
print(user.play("Overwatch", 2))
print(user.buy_game("Risk of Rain 2"))
print(user.buy_game("CSGO"))
print(user.status())

