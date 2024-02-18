class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecture, course, grade):  # Метод выставления оценки лектору студентами
        if isinstance(lecture, Lecture) and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course].append(grade)
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def avarage_grade(self):  # Метод вычисления средней оценки студентов
        self.value_list = []
        for val in self.grades.values():
            for item in val:
                self.value_list.append(item)
        if len(self.value_list) == 0:
            return 0
        return sum(self.value_list) / len(self.value_list)
    
    def __str__(self):  # Метод вывода информации о студенте магическим методом __str__
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avarage_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
    
    def __lt__(self, other):  # Метод сравнения студентов по средней оценке
        if not isinstance(other, Student):
            return
        return self.avarage_grade() < other.avarage_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            return
        return self.avarage_grade() > other.avarage_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return
        return self.avarage_grade() == other.avarage_grade()
    
    def __ne__(self, other):
        if not isinstance(other, Student):
            return
        return self.avarage_grade() != other.avarage_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return
        return self.avarage_grade() <= other.avarage_grade()
    
    def __ge__(self, other):
        if not isinstance(other, Student):
            return
        return self.avarage_grade() >= other.avarage_grade()
  

class Mentor:  # Класс менторов

    def __init__(self, name, surname):  # Инициализация атрибутов родительского класса Mentor
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):  # Класс лекторов

    def __init__(self, name, surname):  # Инициализация атрибутов лектора
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def avarage_grade(self):  # Метод вычисления средней оценки лекторов
        self.value_list = []
        for val in self.grades.values():
            for item in val:
                self.value_list.append(item)
        if len(self.value_list) == 0:
            return 0
        return sum(self.value_list) / len(self.value_list)
    
    def __str__(self):  # Метод вывода информации о лекторе магическим методом __str__
        return f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.avarage_grade()}'
    
    def __lt__(self, other):  # Метод сравнения лекторов по средней оценке
        if not isinstance(other, Lecture) and other != 0:
            return
        return self.avarage_grade() < other.avarage_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avarage_grade() > other.avarage_grade()
    
    def __eq__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avarage_grade() == other.avarage_grade()
    
    def __ne__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avarage_grade() != other.avarage_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avarage_grade() <= other.avarage_grade()
    
    def __ge__(self, other):
        if not isinstance(other, Lecture):
            return
        return self.avarage_grade() >= other.avarage_grade()


class Reviewer(Mentor):  # Класс ревьюров

    def rate_hw(self, student, course, grade):  # Метод выставления оценки студентам
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):  # Метод вывода информации о ревьюре магическим методом __str__
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Ruoy', 'Eman', 'your_gender')   # Создание экземпляров
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Eman', 'Ruoy', 'your_gender')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor2 = Reviewer('Some', 'Buddy')
cool_mentor2.courses_attached += ['Python']

cool_lecture = Lecture('Some', 'Buddy')
cool_lecture.courses_attached += ['Python']

cool_lecture2 = Lecture('Buddy', 'Some')
cool_lecture.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student, 'Python', 9.9)  # Вызов методов выставления оценок студентам
cool_mentor.rate_hw(best_student, 'Python', 9.9)

best_student.rate_lecture(cool_lecture, 'Python', 9.9)  # Вызов методов выставления оценок лекторам
best_student.rate_lecture(cool_lecture, 'Python', 9.9)


def average_grade_for_course(students, course_name):
    grades_sum = 0
    grades_count = 0
    for student in students:
        if course_name in student.grades:
            grades_sum += sum(student.grades[course_name])
            grades_count += len(student.grades[course_name])
    if grades_count == 0:
        return 0
    return grades_sum / grades_count

def average_grade_for_lectures(lecturers, course_name):
    total_grades = 0
    total_lecturers = 0
    for lecture in lecturers:
        if course_name in lecture.grades:
            total_grades += sum(lecture.grades[course_name])
            total_lecturers += len(lecture.grades[course_name])
    if total_lecturers == 0:
        return 0
    return total_grades / total_lecturers


print(cool_mentor)
print(cool_lecture)
print(best_student)

