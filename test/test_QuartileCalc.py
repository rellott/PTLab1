import pytest
from src.QuartileCalc import StudentRatings  # Assuming your class is in a module named student_ratings

# Sample student data for testing
student_data = {
    'Иванов_Иван_Иванович':
        {'математика': 67, 'литература': 100, 'программирование': 91},
    'Петров_Петр_Петрович':
        {'математика': 78, 'химия': 87, 'социология': 61},
    'Сидоров_Сидор_Сидорович':
        {'математика': 78, 'программирование': 85, 'литература': 70},
    'Козлова_Анна_Ивановна':
        {'математика': 95, 'история': 88, 'физика': 72},
    'Зайцев_Захар_Захарович':
        {'математика': 88, 'химия': 75, 'английский': 90},
}


@pytest.fixture
def student_ratings_instance():
    return StudentRatings(student_data)


def test_calculate_rating_percentile(student_ratings_instance):
    subject = 'математика'
    assert student_ratings_instance.calculate_rating_percentile(subject) == 78


def test_get_students_in_first_quartile(student_ratings_instance):
    subject = 'математика'
    students_in_first_quartile = student_ratings_instance.get_students_in_first_quartile(subject)
    expected_students = ['Иванов_Иван_Иванович', 'Петров_Петр_Петрович', 'Сидоров_Сидор_Сидорович']
    assert students_in_first_quartile == expected_students


def test_get_students_in_first_quartile_subject_not_found(student_ratings_instance):
    subject = 'биология'
    with pytest.raises(ValueError, match=r"'биология' отсутствует у всех студентов"):
        student_ratings_instance.get_students_in_first_quartile(subject)
