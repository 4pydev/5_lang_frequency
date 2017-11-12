import sys
import re
from collections import Counter


def load_data(path_to_file):
    with open(path_to_file) as init_file:
        init_text = init_file.read()
    return init_text


def get_most_frequent_words(init_text):
    words_list = re.findall(r'\w+', init_text.lower())
    number_of_words = 10
    ten_most_frequent_words = Counter(words_list).most_common(number_of_words)
    for word in ten_most_frequent_words:
        print(str(word[0]) + " - " + str(word[1]))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        simple_text = load_data(path_to_file)
        get_most_frequent_words(simple_text)
    except IndexError as ind_err:
        print("You must enter the path to file.")
    except OSError as fnf_err:
        print("File not found. You must enter the valid path to file.")
