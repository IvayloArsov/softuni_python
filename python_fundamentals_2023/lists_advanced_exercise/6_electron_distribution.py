def fill_shells(electrons):
    shells = []
    shell_number = 1
    while electrons > 0:
        max_electrons = 2 * shell_number ** 2
        if electrons >= max_electrons:
            shells.append(max_electrons)
            electrons -= max_electrons
        else:
            shells.append(electrons)
            electrons = 0
        shell_number += 1
    return shells


electrons = int(input())
filled_shells = fill_shells(electrons)
print(filled_shells)
