"""
Practice come algebraic equations on sets
"""


def main():
    blue_eyes = {'Olivia', 'Harry', 'Lilly', 'Jack', 'Amelia'}
    blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Josh'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lilly', 'Amelia', 'Lola'}
    o_blood = {'Mia','Josh', 'Lilly', 'Olivia'}
    b_blood = {'Amelia', 'Jack'}
    a_blood = {'Harry',}
    ab_blood = {'Lola'}

    #  Test for Union
    print(blue_eyes.union(blond_hair))
    #  Test Intersection
    print(smell_hcn.intersection(taste_ptc))
    #  Test Difference
    print(smell_hcn.difference(b_blood))
    #  Test Symmetric Difference
    print(blue_eyes.symmetric_difference(o_blood))
    #  Test Symmetric Difference
    print(ab_blood.issubset(taste_ptc))


if __name__ == '__main__':
    main()