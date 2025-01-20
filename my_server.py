from flask import Flask, request, jsonify

app = Flask(__name__)
FILE_PATH = "db.txt"  # File to store data


# GET API: Retrieves the content of the file
@app.route('/file', methods=['GET'])
def get_file_content():
    try:
        with open(FILE_PATH, 'r') as file:
            content = file.read()
        return jsonify({"status": "success", "content": content}), 200
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "File not found."}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# POST API: Writes data to the file
@app.route('/file', methods=['POST'])
def write_to_file():
    try:
        data = request.json.get('data', None)
        if data is None:
            return jsonify({"status": "error", "message": "Missing 'data' in request body."}), 400

        with open(FILE_PATH, 'w') as file:
            file.write(data)
        return jsonify({"status": "success", "message": "Data written to file."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
