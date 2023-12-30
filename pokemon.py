def main():
    user = input('')
    while True:
        querie = input()
        if querie == '':
            exit()
        else:
            pokedex = each_type(user)
            decide(querie, pokedex)

def decide(querie, pokedex):
    '''
    
    Takes the inputted querie and decides which stat will get 
    averaged through the usage of another function. Then the
    Pokemon type with the highest average of the querie 
    will get printed out along with that average.

    Parameters:
    querie - desired stat by user
    pokedex - 2D dictionary containing each pokemon's stats,
    created by another function in the program
    
    Return: prints the Pokemon type that contains the highest
    average of the user's querie
    
    '''
    if querie.lower() == 'total':
        strength_names, highest = total_average(pokedex, 2)
        sorted_names = sorted(strength_names)
        for i in sorted_names:
            print("{}: {}".format(i, highest))
    if querie.lower() == 'hp':
        hp_names, high_hp = total_average(pokedex, 3)
        sorted_names = sorted(hp_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_hp))
    if querie.lower() == 'attack':
        att_names, high_att = total_average(pokedex, 4)
        sorted_names = sorted(att_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_att))
    if querie.lower() == 'defense':
        def_names, high_def = total_average(pokedex, 5)
        sorted_names = sorted(def_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_def))
    if querie.lower() == 'specialattack':
        satt_names, high_satt = total_average(pokedex, 6)
        sorted_names = sorted(satt_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_satt))
    if querie.lower() == 'specialdefense':
        sdef_names, high_sdef = total_average(pokedex, 7)
        sorted_names = sorted(sdef_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_sdef))
    if querie.lower() == 'speed':
        speed_names, high_speed = total_average(pokedex, 8)
        sorted_names = sorted(speed_names)
        for i in sorted_names:
            print("{}: {}".format(i, high_speed))

def each_type(name):
    '''
    
    Reads the csv file provided by the user and creates a
    2D dictionary that will later be used to find the highest
    average.

    Parameter: name - the name of the csv file provided

    Return: a 2D dictionary (pokedex) that contains every
    pokemon, their type, and their stats

    '''
    pokedex = {}
    names = {}
    file = open(name, 'r')
    file.readline()
    for i in file.readlines():
        line = i.strip('\n')
        new_line = line.split(',')
        names[new_line[1]] = new_line[2:]
    for key, value in names.items():
        if value[0] not in pokedex:
            pokedex[value[0]] = {key : value}
        else:
            pokedex[value[0]][key] = value
    return pokedex

def total_average(pokedex, integer):
    '''
    
    Taking the desired querie, the function dissects the 
    pokedex and finds the stat that will then be averaged 
    out.
    
    Parameter: pokedex - a 2D dictionary (pokedex) that contains every
    pokemon, their type, and their stats
    integer - the integer value of the inputted querie that will be 
    used in the 2D dictionary

    Return: a list of the Pokemon type(s) that has the highest average 
    of the desired stat 

    '''
    strength = {}
    for i in pokedex:
        count = 0
        index = 0
        for name in pokedex[i]:
            list = pokedex[i][name]
            count += int(list[integer])
            index += 1
        strength[i] = count / index
    find_max = []
    for number in strength:
        find_max.append(strength[number])
    highest = max(find_max)
    going_back = []
    for name in strength:
        if strength[name] == highest:
            going_back.append(name)
    return going_back, highest

main()
