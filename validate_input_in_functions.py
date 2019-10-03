"""
Program: validate input in functions
Author: Ryan Blankenship
Last Date Modified: 10/3/2019

The purpose of this program is to accept user input
then validate if good or bad input.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: name input by user
    :param test_score: score input by user
    :param invalid_message: message for bad input
    :return:
    """
    try:
        test_score = int(test_score)
    except ValueError:
        return invalid_message

    if test_score < 0 or test_score > 100:
        return invalid_message
    else:
        return test_name + ": " + str(test_score)


if __name__ == '__main__':
    print(score_input("TestScore", 50))
