course_list = input().split(", ")


def check_for_exercise(find_index: int) -> bool:
    try:
        return "Exercise" in course_list[find_index + 1]
    except IndexError:
        return


def add_lesson(lesson_title: str) -> None:
    if lesson_title not in course_list:
        course_list.append(lesson_title)


def insert_lesson(lesson_title: str, index: int) -> None:
    if lesson_title not in course_list:
        course_list.insert(index, lesson_title)


def remove_lesson(lesson_title: str) -> None:
    if lesson_title in course_list:
        find_index = course_list.index(lesson_title)
        if check_for_exercise(find_index):
            del course_list[find_index]
        del course_list[find_index]


def swap_lesson(lesson_title: str, lesson_title_swap: str) -> None:
    if lesson_title in course_list and lesson_title_swap in course_list:
        index_lesson1 = course_list.index(lesson_title)
        index_lesson2 = course_list.index(lesson_title_swap)
        course_list[index_lesson1], course_list[index_lesson2] = \
            course_list[index_lesson2], course_list[index_lesson1]
        if check_for_exercise(index_lesson1):
            course_list.insert(index_lesson2 + 1, course_list.pop(index_lesson1 + 1))
        if check_for_exercise(index_lesson2):
            course_list.insert(index_lesson1 + 1, course_list.pop(index_lesson2 + 1))


def exercise_lesson(lesson_title: str) -> bool:
    if lesson_title in course_list:
        find_index = course_list.index(lesson_title)
        if not check_for_exercise(find_index):
            course_list.insert(find_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in course_list:
        course_list.append(lesson_title)
        course_list.append(f"{lesson_title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lesson,
    "Exercise": exercise_lesson
}

command = input()

while command != "course start":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands[command_type](*info)
    command = input()

for pos, lesson in enumerate(course_list, 1):
    print(f"{pos}.{lesson}")