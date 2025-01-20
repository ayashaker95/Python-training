from flask import Flask, request, jsonify

app = Flask(__name__) # Initializes a new Flask application
FILE_PATH = "db.txt"  # File to store data


# GET the content of the file
@app.route('/file', methods=['GET'])
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
@app.route('/file', methods=['POST'])
def write_to_file():
    try:
        data = request.json.get('data', None) # Extract the data from the json 
        # Condation if the data is NONE 
        if data is None:
            return jsonify({"message": "Missing 'data' in request body."})
        # open the file for write
        with open(FILE_PATH, 'w') as file:
            file.write(data) # Write the the file 
        return jsonify({"message": "Data written to file."})
    except Exception as e:
        return jsonify({"message": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
