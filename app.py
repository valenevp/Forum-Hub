from flask import Flask, request, jsonify
from database import db
from models import User, Course, Topic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/topics', methods=['GET'])
def list_topics():
    topics = Topic.query.all()
    return jsonify([{'id': topic.id, 'title': topic.title, 'message': topic.message, 'user_id': topic.user_id, 'course_id': topic.course_id} for topic in topics])

@app.route('/topics', methods=['POST'])
def create_topic():
    data = request.get_json()
    new_topic = Topic(title=data['title'], message=data['message'], user_id=data['user_id'], course_id=data['course_id'])
    db.session.add(new_topic)
    db.session.commit()
    return jsonify({'id': new_topic.id, 'title': new_topic.title, 'message': new_topic.message, 'user_id': new_topic.user_id, 'course_id': new_topic.course_id}), 201

@app.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'id': new_user.id, 'username': new_user.username}), 201

@app.route('/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'title': course.title} for course in courses])

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(title=data['title'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'id': new_course.id, 'title': new_course.title}), 201

if __name__ == '__main__':
    app.run(debug=True)
