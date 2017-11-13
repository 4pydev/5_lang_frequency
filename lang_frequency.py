import sys
import re
from collections import Counter


def load_data(path_to_file):
    with open(path_to_file) as init_file:
        init_text = init_file.read()
    return init_text


def get_most_frequent_words(init_text, number_of_words):
    words_list = re.findall(r'\w+', init_text.lower())
    most_frequent_words = Counter(words_list).most_common(number_of_words)
    return most_frequent_words


if __name__ == '__main__':
    number_of_words = 10
    try:
        path_to_file = sys.argv[1]
        simple_text = load_data(path_to_file)
        for word, frequency in get_most_frequent_words(simple_text,
                                                       number_of_words):
            print(str(word) + " - " + str(frequency))
    except IndexError as index_error:
        print("You must enter the path to file.")
    except OSError as file_not_found_error:
        print("File not found. You must enter the valid path to file.")
