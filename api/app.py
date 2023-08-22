from flask import Flask, request, jsonify
import graphene
from flask_cors import CORS
from graphql_service.schema import schema

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for the app
CORS(app)


# Define the /graphql endpoint for testing
@app.route("/graphql", methods=["GET", "POST"])
def graphql_server():
    if request.method == "POST":
        data = request.get_json()
    else:  # GET request
        data = request.args

    success = True
    try:
        result = schema.execute(data.get("query"))
        if result.errors:
            response = {"errors": [str(err) for err in result.errors]}
            success = False
        else:
            response = {"data": result.data}
    except Exception as e:
        response = {"errors": [str(e)]}
        success = False
    return jsonify(response), 200 if success else 400


if __name__ == "__main__":
    app.run(debug=True)
