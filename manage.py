from app.main import create_app

# find foods
# @app.route('/find_foods', methods=['GET'])
# def find_foods():
#     body = request.json
#
#     return jsonify(body)

application = create_app()

if __name__ == '__main__':
    application.run(debug=True)
