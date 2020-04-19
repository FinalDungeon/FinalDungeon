"""
This file will contain all the functions and classes required for
the player characters.
"""

from dice import roll

def generate_attributes():

    attribs = list()
    for n in range(6):
        scores = list()
        for i in range (4):
            scores.append(roll('1d6'))
        attribs.append(sum(scores)-min(scores))
    return attribs

def assign_attributes(stats):

    def print_scores(stats):
        print("Scores to assign [Index|Score]")
        for index, score in enumerate(stats):
            print(f"[{index+1} | {score}]", end=' ')
        print()

    ability_scores = {"Strength": 0,
                      "Dexterity": 0,
                      "Constitution": 0,
                      "Intelligence": 0,
                      "Widsom": 0,
                      "Charisma": 0}

    for ability, score in ability_scores.items():
        print_scores(stats)
        selection = input(f"{ability}? ")
        ability_scores[ability] = stats[int(selection)-1]
        stats.pop(int(selection)-1)
        # print(ability_scores)

    return ability_scores


if __name__ == "__main__":

    reroll = True
    while reroll:
        stats = generate_attributes()
        print(f"Your scores are: {stats}")
        again = input("Reroll? (Y/n)")
        if again.lower() == 'n':
            reroll = False

    print(assign_attributes(stats))