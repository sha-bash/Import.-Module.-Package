from main import get_date
from application.salary import calculate_salary
from application.db.people import get_employees
from application.translator import translator

if __name__ == '__main__':
    get_date()
    print('Запуск функции calculate_salary:')
    calculate_salary()
    print('Запуск функции get_employees:')
    get_employees()
    print('Задание 4: ')
    translator()