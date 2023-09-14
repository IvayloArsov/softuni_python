import re

decrypt_key = re.compile(
    r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1: \[(?P<num1>\d+)\]\|\[(?P<num2>\d+)\]\|\[(?P<num3>\d+)\]\|$"
)
rows = int(input())
for row in range(rows):
    cmd_line = input()
    matches = re.match(decrypt_key, cmd_line)
    if matches:
        nums = [(chr(int(num))) for num in matches.groups()[-3:]]
        decrypted_msg = "".join(nums)
        print(f"{matches.group(2)}: {decrypted_msg}")
    else:
        print("Valid message not found!")