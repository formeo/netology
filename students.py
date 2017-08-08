# home work for 1.5 lessons
students = [
    {"name": "Ellen", "surname": "Ripley", "sex": "female", "experienced": 1, "homework": [9, 8, 10, 10, 9], "exam": 10},
    {"name": "Dwayne", "surname": "Hicks", "sex": "male", "experienced": 1, "homework": [9, 8, 8, 9, 9], "exam": 8},
    {"name": "William", "surname": "Hudson", "sex": "male", "experienced": 0, "homework": [9, 8, 6, 5, 8],"exam": 7},
    {"name": "Carter", "surname": "Burke", "sex": "male", "experienced": 1, "homework": [2, 6, 4, 5, 9], "exam": 4},
    {"name": "Jenette", "surname": "Vasquez", "sex": "female", "experienced": 1, "homework": [9, 8, 7, 9, 8], "exam": 8},
    {"name": "Al", "surname": "Apone", "sex": "male", "experienced": 1, "homework": [8, 6, 10, 4, 5], "exam": 6},
    {"name": "Ricco", "surname": "Frost", "sex": "male", "experienced": 1, "homework": [6, 8, 5, 10, 8], "exam": 8},
    {"name": "Colette", "surname": "Ferro", "sex": "female", "experienced": 0, "homework": [4, 7, 9, 3, 6], "exam": 6},
    {"name": "Daniel", "surname": "Spunkmeyer", "sex": "male", "experienced": 1, "homework": [9, 10, 10, 9, 8],"exam": 9},
    {"name": "Tim", "surname": "Crowe", "sex": "male", "experienced": 1, "homework": [7, 6, 4, 5, 9], "exam": 4},
    {"name": "Trevor", "surname": "Wierzbowski", "sex": "male", "experienced": 0, "homework": [9, 6, 3, 5, 8], "exam": 9},
    {"name": "Lance", "surname": "Bishop", "sex": "male", "experienced": 1, "homework": [8, 6, 10, 4, 8], "exam": 10}
]


def get_avg_all():
    avg_hw_sum=0
    avg_exm_sum=0
    for enum in students:
           avg_exm_sum+=enum['exam']
           avg_hw_sum+=sum(enum['homework'])/len(enum['homework'])
    print(("Средняя оценка за домашние задания по группе: {}").format(round(avg_hw_sum/len(students),2)))
    print(("Средняя оценка за экзамен: {}").format(round(avg_exm_sum/len(students),2)))

# Средняя оценка за домашнии работы для своего пола
def get_avg_group_hw_sub_sex(sex):
    sum_avg=0
    sum_sex=0
    for enum in students:
        if enum['sex'] == sex:
            sum_sex+=1
            sum_avg+=sum(enum['homework'])/len(enum['homework'])
    if sum_sex == 0:
        sum_sex = 1
    return round(sum_avg/sum_sex,2)

# Средняя оценка за экзамен для своего пола
def get_avg_group_exm_sub_sex(sex):
    sum_avg = 0
    sum_sex = 0
    for enum in students:
        if enum['sex'] == sex:
            sum_sex += 1
            sum_avg += enum['exam']
    if sum_sex == 0:
        sum_sex = 1
    return round(sum_avg / sum_sex, 2)

# Средняя оценка за домашнии работы для своего експириенса
def get_avg_group_hw_sub_exp(exp):
    sum_avg = 0
    sum_exp = 0
    for enum in students:
        if enum['experienced'] == exp:
            sum_exp+=1
            sum_avg += sum(enum['homework'])/len(enum['homework'])
    if sum_exp == 0:
       sum_exp = 1
    return round(sum_avg / sum_exp, 2)

# Средняя оценка за экзамен для своего експириенса
def get_avg_group_exm_sub_exp(exp):
    sum_avg = 0
    sum_exp = 0
    for enum in students:
        if enum['experienced'] == exp:
            sum_exp+=1
            sum_avg += enum['exam']
    if  sum_exp==0:
        sum_exp=1
    return round(sum_avg /sum_exp, 2)



def get_avg_group():
    print("Средняя оценка за домашние задания у мужчин:",get_avg_group_hw_sub_sex('male'))
    print("Средняя оценка за экзамен у мужчин",get_avg_group_exm_sub_sex('male'))
    print("Средняя оценка за домашние задания у женщин:", get_avg_group_hw_sub_sex('female'))
    print("Средняя оценка за экзамен у женщин",get_avg_group_exm_sub_sex('female'))

    print("Средняя оценка за домашние задания у студентов с опытом:", get_avg_group_hw_sub_exp(1))
    print("Средняя оценка за экзамен у студентов с опытом",get_avg_group_exm_sub_exp(1))
    print("Средняя оценка за домашние задания у студентов без опыта:", get_avg_group_hw_sub_exp(0))
    print("Средняя оценка за экзамен у студентов без опыта",get_avg_group_exm_sub_exp(0))

def get_best_student():
    bs={}
    for enum in students:
         score=round((0.6*sum(enum['homework']))/len(enum['homework'])+0.4*(enum['exam']),2)
         bs[enum['name']+' '+enum['surname']]=score

    max_value = max(bs.values())  # maximum value
    max_keys = [k for k, v in bs.items() if v == max_value]  # getting all keys containing the `maximum`
    if len(max_keys)>1:
        print(("Лучшие студенты: {0} с интегральной оценкой {1}").format( ' , '.join(max_keys),max_value))
    else:
        print(("Лучшие студент: {0} с интегральной оценкой {1}").format(''.join(max_keys), max_value))




functions = {
     'l': get_avg_all,
     'a': get_avg_group,
     'b': get_best_student
}


def check_user_input():
    print(
        "\nl - average exams and homeworks points aLl students "
        "\na - average exams and homeworks point for group sex and experience "
        "\nb – best student"
        "\nq – quit"

       )
    user_input = input('\nвведите команду: ')
    if user_input.lower().strip() in {'l','a','b','q'}:
        return user_input.lower().strip()


# главная функция
def main():
   while True:
     print('Программа учета студентов. ')
     print('Команды:')
     inp=check_user_input()
     if inp == 'q':
         break
     if inp:
         print('')
         functions[inp]()
         print('')



main()
