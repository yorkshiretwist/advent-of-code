import io

file = open('2022/2/input.txt', 'r')
lines = file.readlines()

map_choice = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

map_outcome = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

bonuses = {
    'X': 1, # rock OR lose
    'Y': 2, # paper OR draw
    'Z': 3, # scissors OR win
}

# these will always result in a draw (3 points)
draw_choices = [
    'AX', # rock
    'BY', # paper
    'CZ', # scissors
]

# scores for other outcomes
scores = {
    'YA': 6, # paper defeats rock = 6
    'ZA': 0, # scissors loses to rock = 0
    'XB': 0, # rock loses to paper = 0
    'ZB': 6, # scissors defeats paper = 6
    'XC': 6, # rock defeats scissors = 6
    'YC': 0, # paper loses to scissors = 0
}

# scores for specific outcomes
part_2_choices = {
    'AX': 'Z', # rock, lose
    'AY': 'X', # rock, draw
    'AZ': 'Y', # rock, win
    'BX': 'X', # paper, lose
    'BY': 'Y', # paper, draw
    'BZ': 'Z', # paper, win
    'CX': 'Y', # scissors, lose
    'CY': 'Z', # scissors, draw
    'CZ': 'X', # scissors, win
}

part_1_total = 0

for line in lines:
    parts = line.rstrip().split(' ')
    opponent_choice = parts[0]
    my_choice = parts[1]

    #print(map_choice[opponent_choice] + ' plays ' + map_choice[my_choice])

    part_1_score = 0

    if opponent_choice + my_choice in draw_choices:
        part_1_score = 3
    else:
        part_1_score = scores[my_choice + opponent_choice]

    bonus = bonuses[my_choice]
    part_1_round_total = part_1_score + bonus

    #print(str(part_1_score) + ' + ' + str(bonus) + ' = ' + str(part_1_round_total))
    part_1_total += part_1_round_total

print('Part 1 total: ' + str(part_1_total))

part_2_total = 0

for line in lines:
    parts = line.rstrip().split(' ')
    opponent_choice = parts[0]
    outcome = parts[1]

    #print('Opponent plays ' + map_choice[opponent_choice] + ' - I must ' + map_outcome[outcome])

    part_2_choice = part_2_choices[opponent_choice + outcome]

    part_2_score = 0

    if opponent_choice + part_2_choice in draw_choices:
        part_2_score = 3
    else:
        part_2_score = scores[part_2_choice + opponent_choice]

    bonus = bonuses[part_2_choice]
    part_2_round_total = part_2_score + bonus

    #print(str(part_2_score) + ' + ' + str(bonus) + ' = ' + str(part_2_round_total))
    part_2_total += part_2_round_total

print('Part 2 total: ' + str(part_2_total))