from ..dao.dao import foods_dao


def foods_service(request):
    protein, fat, carb, sugar = request.get("Protein", 0), request.get("Fat", 0), request.get("Carbohydrate", 0), request.get("Sugar", 0)
    food_list = foods_dao(protein, fat, carb, sugar)
    return food_list
