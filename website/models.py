from . import db 
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    school_year = db.Column(db.Integer)
    password = db.Column(db.String(150))
    calendars = db.relationship("Calendar")

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String(10000))

# class Professor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(150), unique=True)
#     rating = db.Column(db.Float)
#     courses = db.relationship("Course")

# class Course(db.Model): #should class sections be separate instances?
#     id = db.Column(db.Integer, primary_key=True)
#     class_code = db.Column(db.String(100), unique=True)
#     class_title = db.Column(db.String(150), unique=True)
#     credit_hour = db.Column(db.Integer)
#     times = db.Column(db.String(150)) #
#     difficulty = db.Column(db.Float)
#     professor_name = db.Column(db.String(100))

# class CalendarCourses(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     calendars = db.relationship("Course")
    
