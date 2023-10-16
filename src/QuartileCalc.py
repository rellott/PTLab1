import numpy as np

class StudentRatings:
    def __init__(self, student_data):
        self.student_data = student_data

    def calculate_rating_percentile(self, subject):
        ratings = [grades.get(subject) for grades in self.student_data.values() if subject in grades]
        if not ratings:
            raise ValueError(f"'{subject}' отсутствует у всех студентов")
        return np.percentile(ratings, 25)

    def get_students_in_first_quartile(self, subject):
        first_quartile_threshold = self.calculate_rating_percentile(subject)
        students_in_first_quartile = []

        for student, grades in self.student_data.items():
            if subject in grades and grades[subject] <= first_quartile_threshold:
                students_in_first_quartile.append(student)

        return students_in_first_quartile


if __name__ == "__main__":
    student_data = {
        'Иванов_Иван_Иванович': {'математика': 67, 'литература': 100, 'программирование': 91},
        'Петров_Петр_Петрович': {'математика': 78, 'химия': 87, 'социология': 61},
        'Сидоров_Сидор_Сидорович': {'математика': 78, 'программирование': 85, 'литература': 70},
        'Козлова_Анна_Ивановна': {'математика': 95, 'история': 88, 'физика': 72},
        'Зайцев_Захар_Захарович': {'математика': 88, 'химия': 75, 'английский': 90},
        # Другие студенты здесь...
    }

    student_ratings = StudentRatings(student_data)
    subject = 'математика'
    students_in_first_quartile = student_ratings.get_students_in_first_quartile(subject)

    print(f"Студенты в первой квартиле по предмету '{subject}':")
    for student in students_in_first_quartile:
        print(student)
