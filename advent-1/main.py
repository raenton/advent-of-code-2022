def find_most_calories():
    calories_totals = []

    with open('input.txt', 'r') as reader:
        counter = 0
        for line in reader:
            if line == '\n':
                calories_totals.append(counter)
                counter = 0
            else:
                counter += int(line)

    return sorted(calories_totals, reverse=True)[0:3]


if __name__ == '__main__':
    total = 0
    for subtotal in find_most_calories():
        total += subtotal

    print(total)
