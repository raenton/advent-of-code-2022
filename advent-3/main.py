def priority(character):
    if character.isupper():
        return ord(character.encode('ascii')) - ord('A'.encode('ascii')) + 1 + 26
    else:
        return ord(character.encode('ascii')) - ord('a'.encode('ascii')) + 1


def common_character(group):
    longest = max(*group, key=len)
    group.remove(longest)
    for char in longest:
        tracker = [False] * len(group)
        for index, item in enumerate(group):
            if char in item:
                tracker[index] = True

        if all(item is True for item in tracker):
            return char


with open('input.txt') as reader:
    total_priority = 0
    processing_group = []
    for line in reader:
        processing_group.append(line.replace('\n', ''))
        if len(processing_group) == 3:
            total_priority += priority(common_character(processing_group))
            processing_group = []

    print(total_priority)
