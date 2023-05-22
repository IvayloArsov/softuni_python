user_input = int(input())


def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    progres = number // 10
    remaining = 10 - progres

    bar = f"{number}% [{'%'*progres}{'.'*remaining}]"
    message = "Still loading..."

    return f"{bar}\n{message}"


print(loading_bar(user_input))