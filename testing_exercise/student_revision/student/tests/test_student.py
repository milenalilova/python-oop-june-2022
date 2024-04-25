from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def test__init__initializes_without_courses(self):
        student = Student('Pepe')
        self.assertEqual('Pepe', student.name)
        self.assertEqual({}, student.courses)

    def test__init__initializes_with_courses(self):
        student = Student('Pepe', {'Python OOP': [6]})
        self.assertEqual('Pepe', student.name)
        self.assertEqual({'Python OOP': [6]}, student.courses)

    def test__enroll__adds_notes_and_returns_correct_message_if_course_in_courses(self):
        student = Student('Pepe', {'Python OOP': [6]})
        result = student.enroll('Python OOP', [5], 'Y')

        self.assertEqual({'Python OOP': [6, 5]}, student.courses)
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test__enroll__returns_correct_message_if_course_notes_y_or_empty(self):
        student = Student('Pepe', {'Python OOP': [6]})
        result = student.enroll('Python Web', [6], 'Y')

        self.assertEqual({'Python OOP': [6], 'Python Web': [6]}, student.courses)
        self.assertEqual('Course and course notes have been added.', result)

        student = Student('Pepe', {'Python OOP': [6]})
        result = student.enroll('Python Web', [6])

        self.assertEqual({'Python OOP': [6], 'Python Web': [6]}, student.courses)
        self.assertEqual('Course and course notes have been added.', result)

    def test__enroll__adds_course_name_without_notes_if_add_course_notes_not_y_or_empty(self):
        student = Student('Pepe', {'Python OOP': [6]})
        student.enroll('Python Web', [6], 'N')
        self.assertEqual({'Python OOP': [6], 'Python Web': []}, student.courses)

    def test__enroll__adds_course_name(self):
        student = Student('Pepe', {'Python OOP': [6]})
        result = student.enroll('Python Web', [6], 'N')
        self.assertEqual({'Python OOP': [6], 'Python Web': []}, student.courses)
        self.assertEqual('Course has been added.', result)

    def test__add_notes__appends_notes_if_course_in_courses(self):
        student = Student('Pepe', {'Python OOP': [6]})
        result = student.add_notes('Python OOP', 5)
        self.assertEqual({'Python OOP': [6, 5]}, student.courses)
        self.assertEqual('Notes have been updated', result)

    def test__add_notes__raises_if_course_not_in_courses(self):
        student = Student('Pepe', {'Python OOP': [6]})
        with self.assertRaises(Exception) as ex:
            student.add_notes('Python Web', 5)
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test__leave_course__pops_course_if_course_in_courses(self):
        student = Student('Pepe', {'Python OOP': [6], 'Python Web': [5]})
        result = student.leave_course('Python Web')
        self.assertEqual({'Python OOP': [6]}, student.courses)
        self.assertEqual('Course has been removed', result)

    def test__leave_course__raises_if_course_not_in_courses(self):
        student = Student('Pepe', {'Python OOP': [6]})
        with self.assertRaises(Exception) as ex:
            result = student.leave_course('Python Web')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == "__main__":
    main()
