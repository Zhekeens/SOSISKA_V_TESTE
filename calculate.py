while(True):
    answer = input("Введите ваше урованений:")
    result = 0
    if('*' in answer):
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


    print(result)