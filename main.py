import os
from datetime import date
from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees
#from application.translator import translator

def logger(old_function):
    def new_function(*args, **kwargs):
        call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = old_function.__name__
        args_str = ', '.join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
        result = old_function(*args, **kwargs)
        log_message = f"[{call_time}] Вызвана функция {func_name} с аргументами: {args_str}. Возвращаемое значение: {result}n"
        
        with open('main.log', 'a') as log_file:
            log_file.write(log_message)
        
        return result
    return new_function

@logger
def get_date():
    current_time = date.today()
    print(current_time)

if __name__ == '__main__':
    get_date()
    print('Запуск функции calculate_salary:')
    calculate_salary()
    print('Запуск функции get_employees:')
    get_employees()
    print('Задание 4: ')
    #translator()
