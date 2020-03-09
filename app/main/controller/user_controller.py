from flask import request, Blueprint, jsonify
from ..service.service import foods_service

user = Blueprint('user', __name__)


@user.route('/foods', methods=['POST'])
def foods():
    body = request.json
    print(body)
    print(type(body))
    print(type(body['Protein']))
    food_list = foods_service(body)

    return jsonify(food_list)
