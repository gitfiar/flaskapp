#!/bin/python 
#coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import datetime, os, time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456@localhost:3306/flask'

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
 
class Models(db.Model):
    __tablename__ = 'Models'

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(80), unique=True)
    Data = db.Column(db.String(256),nullable=False)
    Slgon = db.Column(db.String(128), nullable=False)
    Video = db.Column(db.String(128))
    Thumbnail = db.Column(db.String(128), nullable=False)
    Pictures = db.Column(db.String(256), nullable=False)
    Hometown= db.Column(db.String(80), nullable=False)
    Job= db.Column(db.String(80), nullable=False)
    Creatime = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False) 

    def __init__(self, Name, Data, Slgon, Video, Thumbnail, Pictures, Hometown, Job):
        self.Name = Name
        self.Slgon= Slgon
        self.Data = Data
        self.Pictures=Pictures
        self.Video=Video
        self.Thumbnail=Thumbnail
        self.Hometown=Hometown
        self.Job=Job
        self.PicList=self.getPicArr()
    def getPicArr(self):
        picstr=self.Pictures
        arr=picstr.split('|')
        return arr
    def __repr__(self):
        return '<Models %r>' % self.Name

db.create_all()


