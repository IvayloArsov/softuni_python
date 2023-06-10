
def version_update(version):
    for idx, num in enumerate(reversed(version)):
        if num == 9:
            version[len(version) - idx - 1] = 0
        else:
            version[len(version) - idx - 1] += 1
            break
    return ".".join(map(str, version))


current_version = [int(num) for num in input().split(".")]
updated_version = version_update(current_version)
print(updated_version)