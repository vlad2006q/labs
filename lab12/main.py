import json

class Student:
    def __init__(self, name, group, gpa):
        self.__name = name          # инкапсулированное поле
        self.__group = group
        self.__gpa = gpa

    # --- GETTERS ---
    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def get_gpa(self):
        return self.__gpa

    # --- METHODS ---
    def display_info(self):
        print(f"Студент: {self.__name}, Группа: {self.__group}, GPA: {self.__gpa}")

    def update_gpa(self, new_gpa):
        if 0 <= new_gpa <= 4:
            self.__gpa = new_gpa
        else:
            print("Ошибка: GPA должен быть в пределах 0–4!")

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, name):
        self.students = [s for s in self.students if s.get_name() != name]

    def show_all(self):
        print("\nСписок студентов:")
        for student in self.students:
            student.display_info()

    def get_top_students(self, threshold):
        return [s for s in self.students if s.get_gpa() > threshold]

def save_to_json(group, filename="students.json"):
    data = []
    for s in group.students:
        data.append({
            "name": s.get_name(),
            "group": s.get_group(),
            "gpa": s.get_gpa()
        })
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"\nФайл {filename} успешно сохранён!")

def main():
    group = Group()

    # Пример работы программы
    s1 = Student("Володя", "ИС-22", 3.6)
    s2 = Student("Ерлан", "ИС-23", 2.9)
    s3 = Student("Камила", "ИС-24", 3.95)

    group.add_student(s1)
    group.add_student(s2)
    group.add_student(s3)

    # Показать всех студентов
    group.show_all()

    # Топ студенты (GPA > 3.5)
    print("\nТоп студенты (GPA > 3.5):")
    top = group.get_top_students(3.5)
    for t in top:
        t.display_info()

    # Обновление GPA
    s2.update_gpa(3.2)  # Обновляем GPA у Ерлана
    print("\nПосле обновления GPA Ерлана:")
    group.show_all()

    # Сохранение списка студентов в файл
    save_to_json(group)

if __name__ == "__main__":
    main()