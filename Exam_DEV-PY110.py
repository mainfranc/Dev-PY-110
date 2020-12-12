from random import randint
import json

# 1
def generate_random_add():
    adressDict = read_json_from_the_file()
    for curStreet in adressDict:
        if not validate_streets(adressDict[curStreet]):
            raise Exception(f"The data format in source file is wrong in record {adressDict[curStreet]}")
    while True:
        current_Numbers = ran_numbers(adressDict)
        streetName = adressDict[str(current_Numbers[0])] + ', '
        houseNum = 'д. ' + str(current_Numbers[1]) + ', '
        corp = ""
        if current_Numbers[2]:
            corp = 'корп. ' + str(current_Numbers[2]) + ', '
        fl = 'кв. ' + str(current_Numbers[3])
        yield streetName + houseNum + corp + fl


def read_json_from_the_file():
    with open('streets.json', 'r', encoding='utf8') as f:
        result = json.load(f)
    return result


def validate_streets(in_str):
    if isinstance(in_str, str):
        for i in '\n!,:?':
            if i in in_str:
                return False
        return True
    return False


def ran_numbers(dict_):
    return [randint(0,len(dict_) - 1), randint(1,99), randint(0,3), randint(1,144)]

counter = 0
for i in generate_random_add():
    counter += 1
    print(i)
    if counter > 5:
        break