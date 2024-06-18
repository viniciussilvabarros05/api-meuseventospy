from flask import Flask, request, jsonify
from src.infra.persistence.eventsRepositoryDatabase import EventRepositoryDatabase
from src.infra.persistence.userRepositoryDatabase import UserRepositoryDatabase
from src.app.getAllEventsUsecase import GetAllEventsUseCase
from src.app.createUserUsecase import CreateUserUsecase
from src.core.entity.user import User
from prisma import Prisma
import asyncio

app = Flask(__name__)
db = Prisma()


events = [
    {"id": 1, "name": "Event 1"},
    {"id": 2, "name": "Event 2"},
]

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    email = new_user.get('email')
    name = new_user.get('name')
    user = User(email, name)
    repo = UserRepositoryDatabase(db)
    result = asyncio.run(CreateUserUsecase(repo).execute(user))
    
    return jsonify(result), 200



@app.route('/events/<string:id>', methods=['GET'])
def get_events(id:str):
    repo = EventRepositoryDatabase(db)
    events3 = asyncio.run(GetAllEventsUseCase(repo).execute(id))
    return jsonify(events3), 200

@app.route('/events/<string:id>', methods=['GET'])
def get_event(id: str):
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


@app.route('/events/<string:id>', methods=['PATCH'])
def update_event(id: str):
    event = next((event for event in events if event["id"] == id), None)
    if event:
        updates = request.get_json()
        event.update(updates)
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404


@app.route('/events/<string:id>', methods=['DELETE'])
def delete_event(id: str):
    global events
    events = [event for event in events if event["id"] != id]
    return jsonify({"message": "Event deleted"}), 200


if __name__ == '__main__':
    db.connect()
    app.run(port=3000, debug=True)
