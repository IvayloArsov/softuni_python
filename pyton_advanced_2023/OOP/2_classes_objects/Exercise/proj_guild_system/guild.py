from player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        if player.guild == 'Unaffiliated':
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'
        return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        if all(player.name != player_name for player in self.players):
            return f"Player {player_name} is not in the guild."

        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)
                return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        info_str = [f'Guild: {self.name}']
        for player in self.players:
            info_str.append(f'{player.player_info()}')
        return '\n'.join(info_str)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
