from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False)
    user_pass = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"User(ID = {self.user_id}, name = {self.user_name})"


class DiscordUser(db.Model):
    discord_user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    discord_user_name = db.Column(db.String(50), nullable=False)


class DiscordServer(db.Model):
    discord_server_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    discord_user_id = db.Column(db.Integer, nullable=False)
    discord_server_name = db.Column(db.String(50), nullable=False)
    discord_server_nickname = db.Column(db.String(50))


class DiscordChannel(db.Model):
    discord_channel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    discord_server_id = db.Column(db.Integer, nullable=False)
    discord_channel_name = db.Column(db.String(50), nullable=False)
    discord_channel_mute = db.Column(db.Boolean)


class Planner(db.Model):
    planner_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    planner_name = db.Column(db.String(50), nullable=False)


class Plan(db.Model):
    plan_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    planner_id = db.Column(db.Integer, nullable=False)
    plan_name = db.Column(db.String(50), nullable=False)
    plan_start = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    plan_end = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    repeat = db.Column(db.Boolean)
    repeat_frequency = db.Column(db.DateTime, default=datetime.utcnow)
    repeat_duration = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(250))

    # def __init__(self, planner_id, plan_name, plan_start, plan_end, repeat, repeat_frequency, repeat_duration, description):
    #     self.planner_id = planner_id
    #     self.plan_name = plan_name
    #     # self.plan_start = plan_start
    #     # self.plan_end = plan_end
    #     self.repeat = repeat
    #     # self.repeat_frequency = repeat_frequency
    #     # self.repeat_duration = repeat_duration
    #     self.description = description


class Announcement(db.Model):
    announce_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    discord_channel_id = db.Column(db.Integer, nullable=False)
    plan_id = db.Column(db.Integer, nullable=False)
    announce = db.Column(db.Boolean, nullable=False)
    alert = db.Column(db.DateTime, nullable=False)

db.create_all()