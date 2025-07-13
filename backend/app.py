import os
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# For password hashing
from werkzeug.security import generate_password_hash, check_password_hash
import click

# Get the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app) # This will allow the frontend to make requests to the backend during development

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# A secret key is needed for session management
app.config['SECRET_KEY'] = 'super-secret-key'

db = SQLAlchemy(app)

# Import models after db is defined to avoid circular imports
from models import User, Score

@app.cli.command('init-db')
def init_db_command():
    """Creates the database tables."""
    db.create_all()
    click.echo('Initialized the database.')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 409

    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'New user created!'}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Please check your login details and try again.'}), 401

    session['user_id'] = user.id
    return jsonify({'message': 'Logged in successfully!', 'user': {'id': user.id, 'username': user.username}}), 200

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully!'}), 200

@app.route('/api/scores', methods=['POST'])
def add_score():
    if 'user_id' not in session:
        return jsonify({'message': 'Authentication required'}), 401
    
    data = request.get_json()
    score_value = data.get('score')
    user_id = session['user_id']

    if score_value is None:
        return jsonify({'message': 'Score is required'}), 400

    new_score = Score(score=score_value, user_id=user_id)
    db.session.add(new_score)
    db.session.commit()

    return jsonify({'message': 'Score submitted successfully!'}), 201

@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    top_scores = db.session.query(
        Score.score,
        User.username
    ).join(User).order_by(Score.score.desc()).limit(10).all()

    leaderboard_data = [{'username': username, 'score': score} for score, username in top_scores]
    return jsonify(leaderboard_data), 200


@app.route('/api/hello')
def hello_world():
    return {'message': 'Hello from Flask!'}

if __name__ == '__main__':
    app.run(debug=True) 