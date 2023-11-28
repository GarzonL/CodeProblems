from threading import Timer, Thread
import random

answer = None

operation_list = ['x', '-', '+', '/']
n1 = 0
n2 = 0
def math_game():
    attempt = True
    points = 0
    result = None
    n_questions = 0
    while attempt is True:
        operation = get_operation(n_questions)
        result = get_result_operation(operation)
        input_thread = Thread(target=get_user_input)
        input_thread.start()
        input_thread.join(timeout=3)
        if input_thread.is_alive():
            input_thread.join()
            print("Times is out")
            break
        points += 1 if answer == result else 0
        n_questions += 1
    print(f"Points gained: {points}")
    return True

def get_user_input():
    global answer
    answer = float(input("Please enter the answer: "))

def get_operation(n_questions):
    operation = random.choice(operation_list)
    if n_questions < 6:
        n1 = random.randint(0, 9)
        n2 = random.randint(0, 9)
    elif 5 < n_questions < 11:
        n1 = random.randint(0, 99)
        n2 = random.randint(0, 99)
    elif 10 < n_questions < 16:
        n1 = random.randint(0, 999)
        n2 = random.randint(0, 999)
    else:
        n1 = random.randint(0, 9999)
        n2 = random.randint(0, 9999)
    print(f"Solve this operation: {n1} {operation} {n2}")
    return n1, operation, n2

def get_result_operation(operation_tuple):
    n1, operation, n2 = operation_tuple
    match operation:
        case 'x':
            return n1 * n2
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '/':
            return n1 / n2
        

math_game()