import re

def check_if_match(string, reg):
    """
    check if a string is a choice or not
    :param string: the string to check
    :param reg: regex of choice (A. , a. )
    """
    return bool(re.match(reg, string))


def main():
    # regex = r"[A-Z]\.\s"
    # print(check_if_match(regex, "B. Hôm nay xui quá"))
    # print(check_if_match(regex, "Phát biểu nào sau đây là mệnh đề?"))
    regex = r"[A-Z]\.\s"

    test_str = ("B. Hôm nay xui quá\n"
            "Phát biểu nào sau đây là mệnh đề?")

    matches = re.finditer(regex, test_str)

    for matchNum, match in enumerate(matches, start=1):

        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1

            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

main()
