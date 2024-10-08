from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        # Here, you'd normally insert the data into a database
        return jsonify({'status': 'success'}), 200
    return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
