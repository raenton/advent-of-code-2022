# Opponent: {A, B, C} = {rock, paper, scissors}
# Player: {X, Y, Z} = {rock, paper, scissors}
outcomes = {
    'A': {
        'X': 'D',
        'Y': 'W',
        'Z': 'L'
    },
    'B': {
        'X': 'L',
        'Y': 'D',
        'Z': 'W',
    },
    'C': {
        'X': 'W',
        'Y': 'L',
        'Z': 'D',
    }
}

outcome_scores = {
    'W': 6,
    'D': 3,
    'L': 0
}

choice_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

instruction_to_outcome = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}


def get_outcome(opponent_choice, player_choice):
    return outcomes[opponent_choice][player_choice]


def score_choices(opponent_choice, player_choice):
    return outcome_scores[get_outcome(opponent_choice, player_choice)] + choice_scores[player_choice]


def get_score(opponent_choice, player_instruction):
    target_outcome = instruction_to_outcome[player_instruction]
    for index, (player_choice, outcome) in enumerate(outcomes[opponent_choice].items()):
        if outcome == target_outcome:
            return score_choices(opponent_choice, player_choice)


with open('input.txt') as reader:
    total_score = 0
    for line in reader:
        choices = line.replace('\n', '').split(sep=' ')
        total_score += get_score(choices[0], choices[1])

    print(total_score)


