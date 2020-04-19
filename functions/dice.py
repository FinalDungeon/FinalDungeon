from random import randint

def roll(dice):
    """This function will roll the given number of a specific side die as well as any modifiers
    
    Arguments:
        dice {string} -- The dice that will be rolled
    
    Exaple:
        roll('3d6')
    
    Returns:
        integer -- The result of the dice roll
    """

    # Ensure all characters are lower case
    dice = dice.lower()
    if '+' in dice:
        number, die, bonus = dice.replace('+','d').split('d')
        return randint(int(number),int(number)*int(die)) + int(bonus)
    number, die = dice.split('d')
    return randint(int(number),int(number)*int(die))