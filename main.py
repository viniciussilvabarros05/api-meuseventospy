from flask import Flask, request, jsonify
from src.infra.persistence.eventsRepositoryDatabase import EventRepositoryDatabase
from src.infra.persistence.userRepositoryDatabase import UserRepositoryDatabase
from src.app.getUserByEmailUsecase import GetUserByEmailUseCase
from src.app.getAllEventsUsecase import GetAllEventsUseCase
from src.app.createUserUsecase import CreateUserUsecase
from src.app.createEventUsecase import CreateEventUsecase
from src.app.getEventByIdUsecase import GetEventByIdUseCase
from src.app.deleteEventUsecase import DeleteEventUseCase
from src.app.updateEventUsecase import UpdateEventUseCase
from src.core.entity.user import User
from src.core.entity.event import Event
from prisma import Prisma
from flask_cors import CORS, cross_origin
import asyncio
import uuid

app = Flask(__name__)
CORS(app)
db = Prisma()
EventDatabase = EventRepositoryDatabase(db.event)
UserDatabase = UserRepositoryDatabase(db.user)


@app.route('/user/<string:email>', methods=['GET'])
def login(email):
    result = asyncio.run(GetUserByEmailUseCase(UserDatabase).execute(email))
    
    return jsonify(result.__dict__), 200


@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    email = new_user.get('email')
    name = new_user.get('name')
    id = str(uuid.uuid4())
    user = User(id,email, name)
    result = asyncio.run(CreateUserUsecase(UserDatabase).execute(user))
    print(result)
    if len(result) > 0:
        return jsonify(result), 400
    return jsonify(result), 200


@app.route('/events/<string:id>', methods=['GET'])
def get_events(id: str):
    result = asyncio.run(GetAllEventsUseCase(EventDatabase).execute(id))
    events =  [event.__dict__ for event in result]
    return jsonify(events), 200


@app.route('/event/<string:id>', methods=['GET'])
def get_event(id: str):
    result = asyncio.run(GetEventByIdUseCase(EventDatabase).execute(id))
    if 'error' in result:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(result.__dict__), 200


@app.route('/event', methods=['POST'])
def create_event():
    new_event = request.get_json()
    new_event['id'] =  str(uuid.uuid4()) 
    event = Event(new_event)
    result = asyncio.run(CreateEventUsecase(EventDatabase).execute(event))


    if 'error' in result:
        return jsonify(result), 400
    return jsonify(result), 201


@app.route('/event', methods=['PATCH'])
def update_event():
    event = request.get_json()
    print(event)
    result = asyncio.run(UpdateEventUseCase(EventDatabase).execute(event))
    if 'error' in result:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(result), 200


@app.route('/event/<string:id>', methods=['DELETE'])
def delete_event(id: str):
    result = asyncio.run(DeleteEventUseCase(EventDatabase).execute(id))

    if 'error' in result:
        return jsonify({"error": "Event not found"}), 404
    return jsonify({"status": True}), 200


if __name__ == '__main__':
    db.connect()
    app.run(port=3000, debug=True)
