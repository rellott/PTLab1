from typing import Dict

from DataReader import DataReader
import xml.etree.ElementTree as ET

from Types import DataType


class XMLDataReader(DataReader):
    def read(self, path: str) -> dict[str, dict[str, int]]:
        students = {}

        tree = ET.parse(path)
        root = tree.getroot()

        for student in root:
            student_data = {}
            student_name = student.tag
            for subject in student:
                subject_name = subject.tag
                score = int(subject.text)
                student_data[subject_name] = score
            students[student_name] = student_data

        return students


# Пример использования:
if __name__ == "__main__":
    xml_reader = XMLDataReader()
    data = xml_reader.read("data/data.xml")
    print(data)
