groups = int(input())
teams = {
    'musala': 0,
    'montblanc': 0,
    'kilimanjaro': 0,
    'k2': 0,
    'everest': 0
}
for group in range(1, groups + 1):
    team_size = int(input())

    if team_size <= 5:
        teams['musala'] += team_size
    if 5 < team_size <= 12:
        teams['montblanc'] += team_size
    if 12 < team_size <= 25:
        teams['kilimanjaro'] += team_size
    if 25 < team_size <= 40:
        teams['k2'] += team_size
    if team_size >= 41:
        teams['everest'] += team_size

total_trekkers = sum(teams.values())
print(f"{100 * teams['musala']/total_trekkers:.2f}%")
print(f"{100 * teams['montblanc']/total_trekkers:.2f}%")
print(f"{100 * teams['kilimanjaro']/total_trekkers:.2f}%")
print(f"{100 * teams['k2']/total_trekkers:.2f}%")
print(f"{100 * teams['everest']/total_trekkers:.2f}%")
