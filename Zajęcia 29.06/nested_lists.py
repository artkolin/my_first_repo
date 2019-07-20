"""
Nested lists, sort students
"""

MAX_SCORE = 50

def get_above(students):
    """Print names of students who scored better than 75%"""
    the_best_students = []
    for student in students:
        name = student[0]
        score = student[1]
        score_percentage = score / MAX_SCORE * 100
        if score_percentage >= 75:
            the_best_students.append(student)
    print(the_best_students)


def get_second_best_score(students):
    """Sort students by score, add name to dictionaty"""
    scores_dict = {}
    for student in students:
        name = student[0]
        score = student[1]
        names_list = scores_dict.get(score, [])
        names_list.append(name)
        scores_dict[score] = names_list

    results = sorted(scores_dict.keys(), reverse=True)
    second_score = results[1]
    second_score_students = scores_dict[second_score]
    for name in sorted(second_score_students):
        print(name)


if __name__ == '__main__':
    students_list = [
        ['Sam', 40.5], ['Tom', 49.5], ['Steve', 40.5], ['John', 30.1], ['Arya', 32.2],
    ]
    print(">=75%: ")
    get_above(students_list)
    print("Second best scores: ")
    get_second_best_score(students_list)