from flask import Flask, request, jsonify
from src.infra.persistence.eventsRepositoryDatabase import EventRepositoryDatabase
from src.infra.persistence.userRepositoryDatabase import UserRepositoryDatabase
from src.app.getAllEventsUsecase import GetAllEventsUseCase
from src.app.createUserUsecase import CreateUserUsecase
from src.app.createEventUsecase import CreateEventUsecase
from src.core.entity.user import User
from src.core.entity.event import Event
from prisma import Prisma
import asyncio

app = Flask(__name__)
db = Prisma()
EventDatabase = EventRepositoryDatabase(db.event)
UserDatabase = UserRepositoryDatabase(db.user)

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
    result = asyncio.run(CreateUserUsecase(UserDatabase).execute(user))

    if len(result) > 0:
        return jsonify(result), 400
    return jsonify(result), 200


@app.route('/events/<string:id>', methods=['GET'])
def get_events(id: str):
    result = asyncio.run(GetAllEventsUseCase(EventDatabase).execute(id))
    events = []
    for result in result:
        event = {
            "id":result.id,
            "createdAt":result.createdAt,
            "date":result.date,
            "name":result.name,
            "talks":result.talks,
            "dist":result.dist,
            "local":result.local,
            "author":result.author,
            "userId":result.userId
        }
        events.append(event)
    return jsonify(events), 200


@app.route('/event/<string:id>', methods=['GET'])
def get_event(id: str):
    event = next((event for event in events if event["id"] == id), None)
    if event:
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404


@app.route('/event', methods=['POST'])
def create_event():
    new_event = request.get_json()
    event = Event(new_event)
    result = asyncio.run(CreateEventUsecase(EventDatabase).execute(event))


    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 201


@app.route('/event/<string:id>', methods=['PATCH'])
def update_event(id: str):
    event = next((event for event in events if event["id"] == id), None)
    if event:
        updates = request.get_json()
        event.update(updates)
        return jsonify(event), 200
    return jsonify({"error": "Event not found"}), 404


@app.route('/event/<string:id>', methods=['DELETE'])
def delete_event(id: str):
    global events
    events = [event for event in events if event["id"] != id]
    return jsonify({"message": "Event deleted"}), 200


if __name__ == '__main__':
    db.connect()
    app.run(port=3000, debug=True)
