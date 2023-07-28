import re

pattern = r"(w{3}\.[A-Za-z0-9-\.]+\.[a-z]+)"
line = input()
linx = []
while line:
    matches = re.search(pattern, line)
    if matches:
        linx.append(matches.group(1))
    line = input()
for valid_url in linx:
    print(valid_url)