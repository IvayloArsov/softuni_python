from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.test_student1 = Student('John')
        self.test_student2 = Student('Warren', {'Economics': ['Scamming']})

    def test_successful_init_operation(self):
        self.assertEqual(self.test_student1.name, 'John')
        self.assertFalse(self.test_student1.courses)
        self.assertEqual(self.test_student2.name, 'Warren')
        self.assertIn('Scamming', self.test_student2.courses['Economics'])

    def test_successful_enroll_add_notes_to_existing_course_operation(self):
        result = self.test_student2.enroll('Economics', ['Scheming'])
        self.assertIn('Scheming', self.test_student2.courses['Economics'])
        self.assertEqual(result, 'Course already added. Notes have been updated.')

    def test_successful_enroll_course_plus_notes_with_Y(self):
        result = self.test_student1.enroll('Shopkeeping', ['Just be NPC'], 'Y')
        self.assertIn('Shopkeeping', self.test_student1.courses)
        self.assertEqual(result, "Course and course notes have been added.")

    def test_successful_enroll_course_plus_notes_empty_str(self):
        result = self.test_student1.enroll('Shopkeeping', ['NPC 4 Life'])
        self.assertIn('Shopkeeping', self.test_student1.courses)
        self.assertEqual(result, "Course and course notes have been added.")

    def test_successful_enroll_course(self):
        result = self.test_student1.enroll('Shopkeeping', ['NPC 4 Life'], 'N')
        self.assertEqual(result, "Course has been added.")
        self.assertFalse(self.test_student1.courses['Shopkeeping'])

    def test_unsuccessful_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_student1.add_notes('Bartending', ['Making martini'])
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_successful_add_notes_to_existing_course_in_list(self):
        result = self.test_student2.add_notes('Economics', 'Swindle the fools')
        self.assertEqual(result, "Notes have been updated")
        self.assertIn('Swindle the fools', self.test_student2.courses['Economics'])

    def test_unsuccessful_leave_course_operation_course_not_found(self):
        self.assertNotIn('Barkeeping', self.test_student2.courses)
        with self.assertRaises(Exception) as ex:
            self.test_student2.leave_course('Barkeeping')
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_successful_leave_course_operation(self):
        self.assertIn('Economics', self.test_student2.courses)
        result = self.test_student2.leave_course('Economics')
        self.assertEqual(result, "Course has been removed")
        self.assertNotIn('Economics', self.test_student2.courses)


if __name__ == '__main__':
    main()
