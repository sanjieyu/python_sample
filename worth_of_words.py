# Author:Yi Sun(Tim) 2024-2-21

VALUES = {'e': 1,  'a': 1, 'i': 1, 'o': 1, 'n': 1, 'r': 1,
          't': 1,  'l': 1, 's': 1, 'u': 1, 'd': 2, 'g': 2,
          'b': 3,  'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4,  'w': 4, 'y': 4, 'k': 5, 'j': 8, 'x': 8,
          'q': 10, 'z': 10}


def worth_of_words(words):
    convert_num = []

    for i in range(0,len(words)):
        total_value = 0
        for j in range(0,len(words[i])):
            convert_value = VALUES[words[i][j]]
            total_value = convert_value + total_value
        convert_num.append(total_value)
    final_char = words[convert_num.index(max(convert_num))]
    return final_char

if __name__ == '__main__':
    print("Example:")
    worth_of_words(['hi', 'quiz'])

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz'
    assert worth_of_words(['zero', 'one', 'two', 'three', 'four', 'five']) == 'zero'
    print("Coding complete? Click 'Check' to earn cool rewards!")