class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()

print("Going:", ", ".join(party.people))
print("Total:", len(party.people))