import re
#Баранова Софія КН-31/2
#вихідний словник із даними про студентів
students = {"Іванченко Дмитро Вікторович": {"course": 1, "group": "КН41", "grades": {"Іноземна мова": 82, "Основи академічного письма": 75, "Вища математика": 89, "Вступ до спеціальності": 98, "Дискретна математика": 90, "Організація та обробка електронної інформації": 95}},
            "Захаренко Ольга Миколаївна": {"course": 1, "group": "КН41", "grades": {"Іноземна мова": 92, "Основи академічного письма": 74, "Вища математика": 100, "Вступ до спеціальності": 92, "Дискретна математика": 100, "Організація та обробка електронної інформації": 85}},
            "Бик Іван Єгорович": {"course": 1, "group": "КН42", "grades": {"Іноземна мова": 100, "Основи академічного письма": 87, "Вища математика": 84, "Вступ до спеціальності": 70, "Дискретна математика": 69, "Організація та обробка електронної інформації": 80}},
            "Боровик Ганна Олександрівна": {"course": 1, "group": "КН42", "grades": {"Іноземна мова": 88, "Основи академічного письма": 90, "Вища математика": 66, "Вступ до спеціальності": 94, "Дискретна математика": 75, "Організація та обробка електронної інформації": 89}},
            "Головко Андрій Юрійович": {"course": 2, "group": "КН31", "grades": {"Алгоритми і структури даних": 87, "Математичні методи дослідження операцій": 96, "Організація ІТ-бізнесу": 100, "Програмування мовою Python": 98, "Чисельні методи": 98}},
            "Петренко Юлія Сергіївна": {"course": 2, "group": "КН31", "grades": {"Алгоритми і структури даних": 100, "Математичні методи дослідження операцій": 92, "Організація ІТ-бізнесу": 80, "Програмування мовою Python": 89, "Чисельні методи": 100}},
            "Савченко Григорій Васильович": {"course": 2, "group": "КН32", "grades": {"Алгоритми і структури даних": 80, "Математичні методи дослідження операцій": 82, "Організація ІТ-бізнесу": 76, "Програмування мовою Python": 85, "Чисельні методи": 70}},
            "Гончаренко Оксана Петрівна": {"course": 2, "group": "КН32", "grades": {"Алгоритми і структури даних": 84, "Математичні методи дослідження операцій": 90, "Організація ІТ-бізнесу": 100, "Програмування мовою Python": 95, "Чисельні методи": 72}}}
#список предметів 1-го курсу
subjects1 = ("Іноземна мова", "Основи академічного письма", "Вища математика", "Вступ до спеціальності", "Дискретна математика", "Організація та обробка електронної інформації")
#список предметів 2-го курсу
subjects2 = ("Алгоритми і структури даних", "Математичні методи дослідження операцій", "Організація ІТ-бізнесу", "Програмування мовою Python", "Чисельні методи")

#Баранова Софія КН-31/2
def add_student(students): #функція обробки словника від 1-го студента
    print("\n*додавання нового студента*")
    err = 1
    while err == 1:
        #введення імені студента
        st_name = input("ПІБ -> ")
        a = re.findall("[^((а-яА-ЯіІ)+ )]", st_name)
        if a != []:
            print("некоректні дані")
        else:
            st_name = st_name.title()
            err = 0
    #якщо студент вже є у словнику
    if st_name in students:
        print("студент вже є у словнику")
        return students
    err = 1
    while err == 1:
        #введення курсу
        try:
            st_course = int(input("курс -> "))
        except ValueError:
            print("некоректні дані")
        else:
            if st_course != 1 and st_course != 2:
                print("словник містить дані тільки про студентів 1-го і 2-го курсів")
            else:
                err = 0
    err = 1
    while err == 1:
        #введення групи
        st_group = input("група -> ")
        a = re.findall("[^((а-яА-ЯіІ)+(0-9)+)]", st_group)
        if a != []:
            print("некоректні дані")
        else:
            st_group = st_group.upper()
            err = 0
    print("оцінки")
    if st_course == 1:
        #введення оцінок з предметів 1-го курсу
        st_grades = input_grades(subjects1)
        #створення словника із даними про нового студента
        new_student = dict(course = st_course, group = st_group, grades = st_grades)
    else:
        #введення оцінок з предметів 2-го курсу
        st_grades = input_grades(subjects2)
        #створення словника із даними про нового студента
        new_student = dict(course = st_course, group = st_group, grades = st_grades)
    #додавання нового студента до словника
    students[st_name] = new_student
    print("студента успішно додано до словника")
    print("\nоновлений словник студентів 1-го та 2-го курсів")
    #виведення словника
    for x in students:
        print(f"{x}: курс {students[x]['course']}, група {students[x]['group']}, оцінки {students[x]['grades']}")
    return students
    
#Баранова Софія КН-31/2
def input_grades(subjects): #функція для введення оцінок з предметів
    grades = dict()
    for subject in subjects:
        err = 1
        while err == 1:
            #введення оцінки
            try:
                grade = int(input(f"{subject} -> "))
            except ValueError:
                print("некоректні дані")
            else:
                if grade < 0 or grade > 100:
                    print("оцінка повинна бути в межах від 0 до 100")
                else:
                    #додавання оцінки до словника оцінок
                    grades[subject] = grade;
                    err = 0
    return grades
#Баранова Софія КН-31/2
#виклик функції
students = add_student(students)

#наступному студенту необхідно створити функцію для видалення студента зі словника

#Чернявська Анна КН-32/2
#Видалення студента зі словника
def delete_student(students):
    print("\nВидалення студента:\n")
    while True:
        students_name_for_del = input("Введіть ПІБ студента для видалення: ")
         #Видалення студента, якщо він існує
        if students_name_for_del in students:
            students.pop(students_name_for_del)
            print(f"Студента {students_name_for_del} успішно видалено")
            break
        else:
            #Якщо не знайдено, даємо додатковий шанс на видалення
            print(f"Студента {students_name_for_del} не знайдено")
            while True:
                try:
                    print("Бажаєте спробувати ще раз?\n1. Так\n2. Ні\nВаш вибір: ")
                    opt_choice = int(input())
                    if opt_choice == 1:
                        break
                    elif opt_choice == 2:
                        return students
                    else:
                        print("Невірний вибір, спробуйте ще раз.")
                except ValueError:
                    print("Введіть коректне значення: 1 або 2.")
    #Виведення оновлених даних
    print("Оновлені дані:\n")
    for x in students:
        print(f"{x}: курс {students[x]['course']}, група {students[x]['group']}, оцінки {students[x]['grades']}")
    return students


#Чернявська Анна
#Виклик функції
students = delete_student(students)

#Наступному студенту необхідно створити функцію сортування даних в словнику

#Бєлік Максим КН_32.1
def display_sorted(students): #функція сортування
    print("Оберіть функцію сортування")
    print("1. Сортувати за алфавітом")
    print("2. Сортувати за середніми оцінками")
    choice = input("Оберіть номер функції (1 або 2): ")
    #Вивід за алфавітом
    if choice == '1':
        sorted_students = sorted(students.keys(), key=lambda x: x.lower())
        for student in sorted_students:
            info = students[student]
            print(f"{student}: курс {info['course']}, група {info['group']}, оцінки: {info['grades']}")
    # Вивід за середнім балом
    elif choice == '2':
        avg_grades = []
        for student, info in students.items():
            avg = sum(info['grades'].values()) / len(info['grades'])
            avg_grades.append((student, avg))
        avg_grades.sort(key=lambda x: x[1], reverse=True)
        for student, avg in avg_grades:
            print(f"{student}: (Середня оцінка: {avg:.2f})")
    else:
        print("Невірний вибір. Будь ласка, виберіть 1 або 2.")
        
# Виклик функції
display_sorted(students)

# Наступному студенту застосувати функцію для зміни даних про студента

# Приходько Марія КН-32/2
# Функція для зміни даних про студента 
def change_student(students):
    print("\nЗміна даних про студента\n")
    while True:
        student_name = input("Введіть ПІБ студента для зміни: ")
        if student_name in students:
            print(f"Студент знайдений: {student_name}")
            # Вибір поля для зміни даних
            while True:
                try:
                    print("Що ви хочете змінити?\n1. Курс\n2. Групу\n3. Оцінки\nВаш вибір: ")
                    change_option = int(input()) 
                    if change_option == 1:
                        # Зміна курсу студента
                        new_course = int(input("Введіть новий курс: "))
                        students[student_name]['course'] = new_course
                        print(f"Курс студента {student_name} змінено на {new_course}")
                        break
                    elif change_option == 2:
                        # Зміна групи студента
                        new_group = input("Введіть нову групу: ").upper()
                        students[student_name]['group'] = new_group
                        print(f"Групу студента {student_name} змінено на {new_group}")
                        break
                    elif change_option == 3: 
                        # Зміна оцінок студента
                        if students[student_name]['course'] == 1:
                            # Зміна оцінок для студента 1 курсу
                            students[student_name]['grades'] = input_grades(subjects1) 
                        else:
                            # Зміна оцінок для студента 2 курсу
                            students[student_name]['grades'] = input_grades(subjects2)
                        print(f"Оцінки студента {student_name} оновлено.")
                        break
                    else:
                        # Якщо було обрано невірне значення для операції
                        print("Невірний вибір, спробуйте ще раз.")
                except ValueError:
                    print("Введіть коректне значення: 1, 2 або 3.")
            break
        else:
            # Якщо студента не було знайдено 
            print(f"Студента {student_name} не знайдено.")
    print("Оновлені дані:\n")
    for x in students:
        print(f"{x}: курс {students[x]['course']}, група {students[x]['group']}, оцінки {students[x]['grades']}")
    return students

# Приходько Марія КН-32/2
# Виклик функції
students = change_student(students)

#Наступному студенту необхідно створити функцію для пошуку студентів у словнику 

#Куцевол Аліса КН-32/1
def find_student(students): #функція пошуку студента у словнику
    print("\n*пошук студента*")
    err = 1
    while err == 1:
        find_name = input("Введіть ПІБ студента, якого необхідно знайти: ")#пошук студента за його ПІБ
        a = re.findall(r"[^а-яА-ЯіІїЇєЄ' ]+", find_name)#перевірка на коректність введених даних
        if a:
            print("некоректні дані")
        else:
            if find_name in students:#якщо студента знайдено, виводимо відомості про нього
                print("Відомості про шуканого студента: ")
                print(f"{find_name}: курс {students[find_name]['course']}, група {students[find_name]['group']}, оцінки {students[find_name]['grades']}")
                err = 0
            else:#якщо такого студента немає
                print("Такого студента немає у списку")
                err = 0   
        err=int(input("Хочете знайти ще одного студента? так - 1, ні - 0: "))
    return students

#Куцевол Аліса КН-32/1
#виклик функції
students=find_student(students)