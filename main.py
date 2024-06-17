from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de exemplo para simular um banco de dados
events = [
    {"id": 1, "name": "Event 1"},
    {"id": 2, "name": "Event 2"},
]

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(events), 200

@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event = next((event for event in events if event["id"] == id), None)
    if event:
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404

@app.route('/events', methods=['POST'])
def create_event():
    new_event = request.get_json()
    new_event["id"] = len(events) + 1
    events.append(new_event)
    return jsonify(new_event), 201

@app.route('/events/<int:id>', methods=['PATCH'])
def update_event(id):
    event = next((event for event in events if event["id"] == id), None)
    if event:
        updates = request.get_json()
        event.update(updates)
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404

@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    global events
    events = [event for event in events if event["id"] != id]
    return jsonify({"message": "Event deleted"}), 200

if __name__ == '__main__':
    app.run(port=3000, debug=True)
