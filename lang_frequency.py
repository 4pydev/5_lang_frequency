import sys
import re


def load_data(path_to_file):
    with open(path_to_file) as init_file:
        init_text = init_file.read()
    return init_text


def get_frequencies_dict(init_text):
    words_list = re.split(r'[ _.,:;!?*\—\-\n\\\(\)\[\]\{\}\/\'\"\`\’]+',
                          init_text.lower())

    words_frequencies_dict = {}
    for word in words_list:
        if word not in words_frequencies_dict.keys():
            words_frequencies_dict[word] = 1
        else:
            words_frequencies_dict[word] += 1
    return words_frequencies_dict


def get_most_frequent_words(init_text):
    words_frequencies_dict = get_frequencies_dict(init_text)

    frequencies_list = []
    for key in words_frequencies_dict.keys():
        frequencies_list.append(words_frequencies_dict[key])
    frequencies_list.sort()
    frequencies_list.reverse()

    number_of_words = 10
    for i in range(number_of_words):
        for key in words_frequencies_dict.keys():
            if words_frequencies_dict[key] == frequencies_list[i]:
                print(str(i+1) + " : " + key + ' - ' +
                      str(words_frequencies_dict[key]))


if __name__ == '__main__':
    try:
        path_to_file = sys.argv[1]
        simple_text = load_data(path_to_file)
        get_most_frequent_words(simple_text)
    except IndexError as ind_err:
        print("You must enter the path to file.")
    except OSError as fnf_err:
        print("File not found. You must enter the valid path to file.")
