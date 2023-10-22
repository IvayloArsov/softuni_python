def team_lineup(*players):
    player_count = {}
    for player, country in players:
        player_count[country] = player_count.get(country, 0) + 1

    sorted_countries = sorted(player_count.keys(), key=lambda x: (-player_count[x], x))

    result = []
    for country in sorted_countries:
        players_in_country = [player for player, c in players if c == country]
        result.append(f"{country}:")
        for player in players_in_country:
            result.append(f"  -{player}")

    return "\n".join(result)


print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"), ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany")))
print()
print(team_lineup(("Lionel Messi", "Argentina"), ("Neymar", "Brazil"), ("Cristiano Ronaldo", "Portugal"),
                  ("Harry Kane", "England"), ("Kylian Mbappe", "France"), ("Raheem Sterling", "England")))
print()

print(team_lineup(("Harry Kane", "England"), ("Manuel Neuer", "Germany"), ("Raheem Sterling", "England"),
                  ("Toni Kroos", "Germany"), ("Cristiano Ronaldo", "Portugal"), ("Thomas Muller", "Germany"),
                  ("Bruno Fernandes", "Portugal"), ("Bernardo Silva", "Portugal"), ("Harry Maguire", "England")))


