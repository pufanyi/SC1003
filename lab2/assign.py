from random import shuffle
from typing import List, Tuple


class Student(object):
    def __init__(self, name, email, matriculation_number):
        self.name = name
        self.email = email
        self.matriculation_number = matriculation_number


def assign(
    students_with_preferences: List[List[Student]],
    students_without_preferences: List[Student],
) -> List[List[Student]]:
    # Students without preferences is equivalent to students with preferences with himself as the only preference
    students_with_preferences.extend(
        [[student] for student in students_without_preferences]
    )

    # Shuffle everything to make it fair, randomness introduced here
    # Shuffle groups
    shuffle(students_with_preferences)
    # Shuffle students in groups
    for group in students_with_preferences:
        shuffle(group)

    num_students = sum([len(group) for group in students_with_preferences]) + len(
        students_without_preferences
    )
    num_groups = (num_students + 4) // 5  # ceil(num_students / 5)
    num_4_student_groups = (5 - num_students % 5) % 5
    num_5_student_groups = num_groups - num_4_student_groups

    # Sort out the preferences
    preferences = {
        i: list(
            [
                list(shuffle(group))
                for group in students_with_preferences
                if len(group) == i
            ]
        )
        for i in range(1, 6)
    }


if __name__ == "__main__":
    # Load students preferences, will be implemented later
    pass
