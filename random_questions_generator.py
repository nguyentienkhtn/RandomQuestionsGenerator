import re
question_choice_format = '[A-Z]. '
number_of_choices = 4


def check_if_a_choice(string, reg):
    """
    check if a string is a choice or not
    :param string: the string to check
    :param reg: regex of choice (A. , a. )

    """
    return bool(re.match(reg, string))


def main():
    questions = {}
    file = open(r"testRandom.txt",encoding='utf-8')
    line = file.readline()
    question_text = ''
    choices = []
    answer = ''
    while line != '':
        
        if (not(line.startswith('ANSWER'))) and \
                (not(check_if_match("[A-Z]. ",line))): # a question text
            question_text = line
        elif check_if_match(question_choice_format,line): # it's a choice
            choices.append(line)
        else: # it's an answer
            answer = line
        if len(choices) == number_of_choices:
            questions[question_text] = [choices, answer]
            question_text = ''
            choices = []
            answer = ''

        line = file.readline()
    print(questions)


main()
