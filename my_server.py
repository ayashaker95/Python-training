from flask import Flask, request, jsonify

app = Flask(__name__)  # Initializes a new Flask application
FILE_PATH = "db.txt"  # File to store data

username = "admin"
password = "admin"

def is_authenticated():
    auth = request.authorization
    return auth and auth.username == username and auth.password == password

def authentication():
    return jsonify({"message": "Authnication required "})

# GET the content of the file


@app.route('/test-get-api', methods=['GET'])
def get_file_content():
    try:
        # Open the file for read
        with open(FILE_PATH, 'r') as file:
            content = file.read()
            # Return the data
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"message": str(e)})


# POST data to the file
@app.route('/test-post-api', methods=['POST'])
def write_to_file():
    if not is_authenticated():
        return authentication()
    try:
        data = request.json.get('data', None)  # Extract the data from the json
        if data is None: # Condation if the data is NONE
            return jsonify({"message": "Missing data in request body."})
        # open the file for write
        with open(FILE_PATH, 'w') as file:
            file.write(data)  # Write the the file
            return jsonify({"message": "Data written to the file."})
    except Exception as e:
        return jsonify({"message": str(e)})

# PUT Request
@app.route('/test-put-api', methods=['PUT'])
def update_file():
        if not is_authenticated():
            return authentication()
        try:
            data = request.json.get('data', None)  # Extract the data from the JSON
            if data is None:
                return jsonify({"message": "Missing data in request body."})
            with open(FILE_PATH, 'w') as file:
                file.write(data)  # Overwrite the file with new data
                return jsonify({"message": "File updated successfully."})
        except Exception as e:
            return jsonify({"message": str(e)})

# PATCH Request
@app.route('/test-patch-api', methods=['PATCH'])
def append_to_file():
        if not is_authenticated():
            return authentication()
        try:
            data = request.json.get('data', None)  # Extract the data from the JSON
            if data is None:
                return jsonify({"message": "Missing data in request body."})
            with open(FILE_PATH, 'a') as file:
                file.write(data)  # Append the data to the file
                return jsonify({"message": "Data appended to the file."})
        except Exception as e:
            return jsonify({"message": str(e)})

# DELETE Request
@app.route('/test-delete-api', methods=['DELETE'])
def delete_file():
        if not is_authenticated():
            return authentication()
        try:
            import os
            if os.path.exists(FILE_PATH):
                os.remove(FILE_PATH)  # Delete the file
                return jsonify({"message": "File deleted successfully."})
            else:
                return jsonify({"message": "File does not exist."})
        except Exception as e:
            return jsonify({"message": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
