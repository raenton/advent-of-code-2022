def priority(character):
    if character.isupper():
        return ord(character.encode('ascii')) - ord('A'.encode('ascii')) + 1 + 26
    else:
        return ord(character.encode('ascii')) - ord('a'.encode('ascii')) + 1


def common_character(string_pair):
    for char in string_pair[0]:
        if char in string_pair[1]:
            return char


def cut_in_half(line):
    first, second = line[:len(line)//2], line[len(line)//2:]
    return first, second


with open('input.txt') as reader:
    total = 0
    for line in reader:
        total += priority(common_character(cut_in_half(line)))

    print(total)
