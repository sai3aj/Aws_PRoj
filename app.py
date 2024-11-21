from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/appointments', methods=['POST'])
def book_appointment():
    data = request.json
    email = data.get('email')
    car_model = data.get('carModel')
    date = data.get('date')

    # TODO: Add logic to store the appointment in DynamoDB
    # Example: response = add_appointment(email, car_model, date)

    return jsonify({"message": "Appointment booked successfully!"}), 201

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
