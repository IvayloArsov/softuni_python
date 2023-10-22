def students_credits(*courses):
    result = []
    goal = 240
    total_credits = 0
    split_courses = [course.split('-') for course in courses]
    course_details = []

    for course in split_courses:
        course_name = course[0]
        credits_, max_pts, score_pts = (int(f) for f in course[1:])
        score = score_pts/max_pts
        given_credits = credits_ * score
        total_credits += given_credits
        course_details.append((course_name, given_credits))
    course_details.sort(key=lambda x: x[1], reverse=True)

    for course, credits in course_details:
        result.append(f'\n{course} - {credits:.1f}')
    if total_credits >= goal:
        result.insert(0, f'Diyan gets a diploma with {total_credits:.1f} credits.')
    else:
        result.insert(0, f'Diyan needs {goal-total_credits:.1f} credits more for a diploma.')
    return ''.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)