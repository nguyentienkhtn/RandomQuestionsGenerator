import re
import random

number_of_choices = 4


def check_if_a_choice(string):
    """
    check if a string is a choice or not
    :param string: the string to check
    """
    if string[0].isupper() and string[1] == "." \
            and (string[2] == ' ' or string[2] == '\t'):
        return True
    else:
        return False


def main():
    # st1 = "Phát biểu nào sau đây là mệnh đề?"
    # st2 = "A. Hôm nay trời xám xịt"
    # print(check_if_a_choice(st2))
    # print(check_if_a_choice(st1))
    question = {}
    questions = []
    file = open(r"testRandom.txt",encoding='utf-8')
    line = file.readline()
    question_text = ''
    choices = []
    answer = ''
    while line != '':
        if (not(line.startswith('ANSWER'))) and \
                (not(check_if_a_choice(line))): # a question text
            question_text = line
        elif check_if_a_choice(line): # it's a choice
            choices.append(line[2:])
        else: # it's an answer
            answer = line
        if len(choices) == number_of_choices and answer != '':
            question["Câu hỏi: " + question_text] = [choices]
            questions.append(question)
            question = {}
            question_text = ''
            choices = []
            answer = ''

        line = file.readline()
    print(questions)
    random.shuffle(questions)
    print(questions)
    for question_temp in questions:
        print(type(question_temp.values()))
        random.shuffle(question_temp.values())
        print("hello", question_temp)

    print(questions)


main()
# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)
#
# print(mylist)