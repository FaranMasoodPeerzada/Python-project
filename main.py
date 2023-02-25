import re
from collections import Counter


def read_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f:
        text = f.read()
    return text

def get_start_end_indexes(text):
    start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
    end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
    start_index = text.find(start_marker)
    end_index = text.find(end_marker)
    if start_index == -1 or end_index == -1:
        raise Exception("Start or end marker not found")
    start_index = text.find('\n', start_index) + 1
    end_index = end_index - 1
    return start_index, end_index

def get_text_without_markers(text, start_index, end_index):
    return text[start_index:end_index]


def read_without_makers_file(new_file):
    with open(new_file, 'r') as file:
        new_text = file.read()
    return new_text


def get_word_list(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    word_list = text.split()
    return word_list

def get_two_word_sequences(word_list):
    two_word_sequences = []
    for i in range(len(word_list) - 1):
        two_word_sequence = word_list[i] + ' ' + word_list[i + 1]
        two_word_sequences.append(two_word_sequence)
    #print(f'The bigrams in the text are: {two_word_sequences}')
    return two_word_sequences

def get_ten_most_frequent(two_word_sequences):
    two_word_sequence_counts = Counter(two_word_sequences)
    five_most_frequent = two_word_sequence_counts.most_common(10)
    return five_most_frequent

def main(file_name):
    text = read_file(file_name)
    start_index, end_index = get_start_end_indexes(text)
    text_without_markers = get_text_without_markers(text, start_index, end_index)
    with open('text_without_markers.txt', 'w') as f:
        f.write(text_without_markers)
    print('Text without markers has been saved to text_without_markers.txt')
    without_markers_text = read_without_makers_file(new_file='text_without_markers.txt')
    word_list = get_word_list(without_markers_text)
    two_word_sequences = get_two_word_sequences(word_list)
    five_most_frequent = get_ten_most_frequent(two_word_sequences)
    print('\nThe ten most frequent two-word sequences are:')
    for sequence, count in five_most_frequent:
        print(f'{sequence}: {count}')

if __name__ == '__main__':
    file_name = 'book.txt'
    main(file_name)
