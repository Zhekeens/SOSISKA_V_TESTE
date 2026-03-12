import math
while(True):
    answer = input("Введите ваше урованений:")
    result = 0
    if ('*' in answer):
        answer = answer.split('*')
        result = int(answer[0]) * int(answer[1])
    elif '-' in answer:
        answer = answer.split('-')
        result = int(answer[0]) - int(answer[1])
    elif '/' in answer:
        answer = answer.split('/')
        result = int(answer[0]) / int(answer[1])
    elif '+' in answer:
        answer = answer.split('+')
        result = int(answer[0]) + int(answer[1])
    elif '**' in answer:
        answer = answer.split('**')
        result = int(answer[0]) ** int(answer[1])
    elif '|' in answer:
        answer = answer.split('|')
        result = math.sqrt(int(answer[0]))
    elif 'fac' in answer:
        factorial = 1
        number = answer.split('fac')

        for i in range(2, int(number[1]) + 1):
            factorial *= i
            result = factorial

    print("Привет земляне")
    print(result)