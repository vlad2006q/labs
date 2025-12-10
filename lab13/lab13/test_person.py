import unittest
from main import Student, Teacher, AdminStaff, Person


class TestStudent(unittest.TestCase):
    def test_gpa_range(self):
        s = Student("Алиса", 19, "IS-23", 3.7)
        self.assertTrue(0 <= s.gpa <= 4.0)

    def test_display(self):
        s = Student("Алиса", 19, "IS-23", 3.5)
        self.assertIn("IS-23", s.display_info())


class TestTeacher(unittest.TestCase):
    def test_experience(self):
        t = Teacher("Эрик", 40, "Math", 10)
        self.assertEqual(t.experience, 10)


class TestAdminStaff(unittest.TestCase):
    def test_department(self):
        a = AdminStaff("Олег", 30, "Инженер", "Технический отдел")
        self.assertEqual(a.department, "Технический отдел")


if __name__ == "__main__":
    unittest.main()