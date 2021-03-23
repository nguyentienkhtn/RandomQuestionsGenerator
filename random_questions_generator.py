import re
import random
import codecs
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
    questions = [] # list of dictionaries
    file = open(r"testRandom.txt", encoding='utf-8')
    line = file.readline()
    question_text = ''
    choices = []
    answer = ''
    while line != '':
        if (not (line.startswith('ANSWER'))) and \
                (not (check_if_a_choice(line))):  # a question text
            question_text = line
        elif check_if_a_choice(line):  # it's a choice
            choices.append(line[3:])
        else:  # it's an answer
            answer = line
        if len(choices) >= 2 and answer != '':
            question[question_text] = choices
            questions.append(question)
            question = {}
            question_text = ''
            choices = []
            answer = ''

        line = file.readline()
    # print("original:", questions)
    random.shuffle(questions)
    # print(questions)
    # f = open(r"result.txt", encoding='utf-8')
    with codecs.open("result.txt", "w", "utf-8-sig") as temp:
        for question_temp in questions:
            '''
            shuffle choices
            '''
            answers = list(question_temp.values())[0]
            random.shuffle(answers)
            print(type(list(question_temp.keys())[0]))
            # write answer text
            temp.write(list(question_temp.keys())[0])
            for t in answers:
                temp.write(t)
            temp.write('\n')

    # print(questions)


main()
