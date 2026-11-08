# Function to calculate average grades
def get_average_grade(grades_tuple):
    try:
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
        return None

# Dictionary containing courses and grades
course_grades = {
    "Math": (90, 85, 80),
    "Science": (88, 92, 95),
    "History": (75, 80, 85),
    "English": ()
}

# Loop through each course
for course, grades in course_grades.items():
    average = get_average_grade(grades)

    if average is None:
        print("No grades available for", course)
    else:
        print("The average grade for", course, "is", round(average, 2))