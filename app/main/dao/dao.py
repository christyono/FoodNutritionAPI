import json
import os
from collections import defaultdict


def foods_dao(p, f, c, s):
    # connect to db, but in this case we're just parsing a file.
    file = open(os.getcwd() + '\\app\\food_data.json')
    data = json.load(file)
    # retrieve foods from database(the file)
    food_list = data['report']['foods']


    '''
    our goal here is to parse through the foods, add names of food that satisfy query conditions to ret list.
    
    following condition(s) must be satisfied:
        food's nutrition(s) must have gram amount > amount specified by user.
    
    in some cases, gram amount(gm) is unspecified, indicated by '--'. 
    Thus, gm can be either type 'str' or 'float'. This needs to be accounted for.
    '''
    ret = []
    # iterate through the foods
    for food in food_list:
        name = food['name']
        nutrients = food['nutrients']
        # iterate through nutrients in each food. we're looking for Protein(203), Fat(204), Carbs(205), and Sugar(269)

        query = defaultdict()
        for nutrient in nutrients:
            if nutrient['nutrient_id'] == '203':
                query['Protein'] = nutrient['gm']
            if nutrient['nutrient_id'] == '204':
                query['Fat'] = nutrient['gm']
            if nutrient['nutrient_id'] == '205':
                query['Carbs'] = nutrient['gm']
            if nutrient['nutrient_id'] == '269':
                query['Sugar'] = nutrient['gm']
        # compare
        if type(query['Protein']) == str or query['Protein'] <= p:
            continue
        if type(query['Fat']) == str or query['Fat'] <= f:
            continue
        if type(query['Carbs']) == str or query['Carbs'] <= c:
            continue
        if type(query['Sugar']) == str or query['Sugar'] <= s:
            continue

        # if all conditions are satisfied, add to the list
        ret.append(food)

    file.close()
    return ret
