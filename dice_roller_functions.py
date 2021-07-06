import random as r

class DiceRoller():

    def two_sided_roll():
        result = r.randint(1, 2)
        return result

    def four_sided_roll():
        result = r.randint(1, 4)
        return result

    def six_sided_roll():
        result = r.randint(1, 6)
        return result

    def eight_sided_roll():
        result = r.randint(1, 8)
        return result

    def ten_sided_roll():
        result = r.randint(1, 10)
        return result

    def twelve_sided_roll():
        result = r.randint(1, 12)
        return result

    def twenty_sided_roll():
        result = r.randint(1, 20)
        return result
        