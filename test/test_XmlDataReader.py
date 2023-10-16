from src.XmlDataReader import XMLDataReader  # Импортируем класс, который нужно протестировать


# Параметризованный тест для проверки чтения данных из XML-файла
def test_xml_data_reader():
    xml_reader = XMLDataReader()

    # Путь к тестовому XML-файлу с данными
    test_xml_path = "test/test.xml"

    # Ожидаемые результаты чтения данных из XML-файла
    expected_data = {
        "Alice": {"Math": 95, "History": 85, "English": 90},
        "Bob": {"Math": 88, "History": 92, "English": 89}
    }

    # Вызываем метод read() и проверяем, соответствуют ли фактические результаты ожидаемым
    assert xml_reader.read(test_xml_path) == expected_data
