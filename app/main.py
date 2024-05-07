from flask import Flask, jsonify, request

app = Flask(__name__)

data = [{"name": "Poorna", "location": "Bangalore"},
        {"name": "Raj", "location": "Mysore"},
        {"name": "Kumar", "location": "Chennai"}]


@app.route('/')  # decorator
def hello_world():
    # view function
    return 'Hello, World!'

@app.route('/data')
def get_data():
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)