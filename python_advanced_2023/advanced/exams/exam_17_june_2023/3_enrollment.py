def gather_credits(needed_credits, *courses):
    enrolled_courses = []
    total_credits = 0

    for course in courses:
        course_name, course_credits = course
        if total_credits < needed_credits:
            if course_name not in enrolled_courses:
                enrolled_courses.append(course_name)
                total_credits += course_credits

    if total_credits >= needed_credits:
        enrolled_courses.sort()
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(enrolled_courses)}"
    else:
        credits_shortage = needed_credits - total_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))