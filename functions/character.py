"""
This file will contain all the functions and classes required for
the player characters.
"""

from dice import roll
import json

def generate_attributes():
    """Get six scores for the player to assign and allow for rerolls

    Returns:
        list -- attribs is a list of six scores to be assigned later
    """
    reroll = True
    while reroll:
        attribs = list()
        for n in range(6):
            scores = list()
            for i in range (4):
                scores.append(roll('1d6'))
            attribs.append(sum(scores)-min(scores))
        print(f"Your scores are: {attribs}")
        again = input("Reroll? (Y/n)")
        if again.lower() == 'n':
            reroll = False
    return attribs

def assign_attributes(stats):
    """Function to assign the six ability scores to the six attributes

    Arguments:
        stats {list} -- A list of six integers that will be used to assign to the attributes

    Returns:
        dict -- A dictionary of the six attributes and the assign scores
    """
    def print_scores(stats):
        """Sub fucntion to print out the scores to still be assigned
        
        Arguments:
            stats {list} -- A list of interegers that still need to be assigned
        """
        print("Scores to assign [Index|Score]")
        for index, score in enumerate(stats):
            print(f"[{index+1} | {score}]", end='')
        print()

    ability_scores = {"strength": 0,
                      "dexterity": 0,
                      "constitution": 0,
                      "intelligence": 0,
                      "widsom": 0,
                      "charisma": 0}
    
    for ability, score in ability_scores.items():
        print_scores(stats)
        selection = input(f"{ability}? ")
        ability_scores[ability] = stats[int(selection)-1]
        stats.pop(int(selection)-1)

    return ability_scores

def ability_bonuses(ability_scores):
    """This function will be used to determine the ability bonus for each attribute and assign
    them to a tuple with the ability score to the proper attribute

    Arguments:
        ability_scores {dict} -- The currect dictionary of the attributes and thier ability scores

    Returns:
        dict -- The dictionary updated with the bonus an score creating a tuple and assigned to
        the proper attribute
    """
    for ability, score in ability_scores.items():
        bonus = (score-10)//2
        ability_scores[ability] = (score, bonus)

    return ability_scores

def select_race(races, ability_scores):
    """In order to get the final ability scores, we will need to know the characters race
    
    Arguments:
        races {dict} -- A dictionary containing the racial information loaded in from the
        races.json file in the data folder
        ability_scores {dict} -- The current value of the characters ability scores so they
        can be modified by racial modifiers
    
    Returns:
        dict -- A dictionary with the characters race
        dict -- A dictionary with the modified ability scores
    """

    race_list = ['Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling', 'Human']
    for index, race in enumerate(race_list):
        print(f"[{index+1} | {race}]", end='')
    print()
    selection = input('Select a race: ')
    race = races['race'][race_list[int(selection)-1].lower()]

    for ability, modifier in race['abilitymod'].items():
        ability_scores[ability] = ability_scores[ability] + modifier

    return race, ability_scores

def main():
    """Main to run all ability score generation in one place
    """

    with open('./functions/data/races.json') as races_file:
        races = json.load(races_file)
    stats = generate_attributes()
    ability_scores = assign_attributes(stats)
    print(ability_scores)
    race, ability_scores = select_race(races, ability_scores)
    ability_scores = ability_bonuses(ability_scores)
    print(ability_scores)


if __name__ == "__main__":
    main()