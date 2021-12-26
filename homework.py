class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grades(self):
        sum_gr = 0
        lenght = 0
        for course, num in self.grades.items():
            sum_gr += sum(self.grades[course])
            lenght += len(num)
        return(round((sum_gr / lenght), 2))

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
   
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 
    
    def average_grades(self):
        sum_gr = 0
        lenght = 0
        for course, num in self.grades.items():
            sum_gr += sum(self.grades[course])
            lenght += len(num)
        return(round((sum_gr / lenght), 2))

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.average_grades() < other.average_grades()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}'
      

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
      
def get_avg_st_grade(students_list, courses):
    all_sum = 0
    for student in students_list:
        sum_gr = 0
        lenght = 0
        for course, num in student.grades.items():        
            if course == courses:
                sum_gr += sum(student.grades[course])
        lenght += len(num)
        all_sum += sum_gr / lenght
    return all_sum 

def get_avg_lec_grade(lecturer_list, courses):
    all_sum = 0
    for lecturer in lecturer_list:
        sum_gr = 0
        lenght = 0
        for course, num in lecturer.grades.items():        
            if course == courses:
                sum_gr += sum(lecturer.grades[course])
        lenght += len(num)
        all_sum += sum_gr / lenght
    return all_sum 
        
student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.finished_courses += ['Введение в программирование']
student1.courses_in_progress += ['Python', 'Git']

student2 = Student('No', 'Buddy', 'your_gender')
student2.finished_courses += ['Введение в программирование']
student2.courses_in_progress += ['Pithon', 'Git']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Someone', 'Else')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1 = Reviewer('No', 'buddy')
reviewer1.courses_attached += ['Python', 'Git']

reviewer2 = Reviewer('Not', 'me')
reviewer2.courses_attached += ['Python', 'Git']

student1.rate_lec(lecturer1, 'Python', 9)
student1.rate_lec(lecturer2, 'Git', 8)

student2.rate_lec(lecturer1, 'Python', 10)
student2.rate_lec(lecturer2, 'Git', 8)

reviewer1.rate_hw(student1, 'Python',10)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Git', 10)

reviewer2.rate_hw(student1, 'Python',10)
reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Git', 10)

print(student1)
print(student2)
print(student1 < student2)

print(lecturer1)
print(lecturer2)
print(lecturer1 < lecturer2)

print(reviewer1)
print(reviewer2)

student_list = [student1, student2]
print(get_avg_st_grade(student_list, 'Git'))

lecturer_list = [lecturer1, lecturer2]
print(get_avg_lec_grade(lecturer_list, 'Git'))