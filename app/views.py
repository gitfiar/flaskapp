##!/bin/python 
#coding:utf-8 -*- coding: utf-8 -*-
from flask import Blueprint, render_template, session,  flash, redirect, url_for, request, send_from_directory, jsonify, Response
from flask import Flask
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    StringField, BooleanField, SubmitField, IntegerField, FormField, SelectField	
from wtforms.validators import Required, DataRequired, Length, Regexp
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf.file import FileField, FileRequired, FileAllowed
import os
import re
#  from db import Users
from flask_bootstrap import Bootstrap
#  from models import db, Models
from os import path
#  from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
from app.models import db, Models
from sqlalchemy import not_
from numpy import *
from wtforms.validators import Length,DataRequired
from app.sms import Sms
from datetime import timedelta
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456@localhost:3306/flask'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/upload_file/'
app.config['UPLOADED_IMAGES_DEST']= os.getcwd()+'/upload_file/'
UPLOAD_FOLDER =  os.getcwd() + '/upload_file/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)

class LoginForm(FlaskForm):
    toNumber = StringField(u"手机号码",validators=[Regexp('^[1][3-8][0-9]{9}$',flags=re.I,message=u"请输入正确手机号码")])
 
    smsCode =  TextField(u"验证码", validators=[Required()])

    subBtn = SubmitField(u"获取验证码", validators=[Required()])
    submit = SubmitField(u"注册", validators=[Required()])

#  db=SQLAlchemy(app)
#  db.create_all()
class AddForm(FlaskForm):
    Name = TextField(u"名字", validators=[Required()])
    Data = TextField(u"资料", validators=[Required()])
    Slgon = TextField(u"特点", validators=[Required()])
    Hometown = TextField(u"籍贯", validators=[Required()])
    Job = TextField(u"职业", validators=[Required()])
    Thumbnail =SelectField(u'缩略图', choices=[], coerce=int)    #  thum = TextField("Thum", validators=[Required()])
    Video = TextField(u"视频", validators=[Required()])
    Pictures = TextField(u"图片", validators=[Required()])
    
views = Blueprint('views', __name__)

photos = UploadSet('images', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB

class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image Only!'), FileRequired(u'Choose a file!')])
    submit = SubmitField(u'Upload')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPEG', 'GIF', 'JPG', 'MP4', 'mov', 'MOV'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def is_login(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        cook = request.cookies.get("status")
        if cook:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('.login'))
    return check_login


@views.route('/login', methods=['GET', 'POST'])
def login():
    resp = Response("服务器返回信息")
    #设置cookie，
    ip = request.remote_addr
    form = LoginForm()
    return render_template('login.html',user_ip=ip,form=form)

@views.route('/checkcode', methods=['GET', 'POST'])
def checkCode():
        aNum = request.args.get('toNumber')
        aCode = request.args.get('smsCode')
        mid = request.args.get('mId')
        print "ate ：：：%s : %s : %s" %(aNum , aCode ,mid)
        #  num c = request.form['toNumber']
        client = Sms(aNum)
        bCode = client.getHisCode(mid)
        bNum = int(mid)-bCode
        print 'bte::::::%s : %s' %(bNum ,bCode)
        if int(aNum) == bNum and int(aCode) == bCode :
            print u"验证成功"
            return jsonify({"result":1})
        else:
            print u"验证失败"
            return redirect(url_for("login"))


@views.route('/sendcode', methods=['GET', 'POST'])
def sendCode():
        num = request.args.get('toNumber')
        #  num c = request.form['toNumber']
        print num
        client = Sms(num)
        client.randomCode()
        res = client.send()
        print res
        success= res['code']
        mId=client.messageId if res['code']==0 else ''
        return jsonify({"result":success,'mId':mId})




@views.route('/', methods=['GET', 'POST'])
#  @is_login
def index():
        dirpath=path.abspath(path.dirname(__file__))
        mo =Models.query.order_by(Models.Id.desc()).all()
        l='#items'
        return render_template('index.html',dirpath=app.config['UPLOAD_FOLDER'],link=l  ,uers=mo)
        #return redirect(url_for('.login'))

@views.route('/new', methods=['GET', 'POST'])
def new():
    dirpath=path.abspath(path.dirname(__file__))
    mo =Models.query.order_by(Models.Id.desc()).all()
    l='#items'
    return render_template('new.html',dirpath=app.config['UPLOAD_FOLDER'],link=l  ,uers=mo)




@views.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        form = AddForm()
        Model = Models(
            Name=request.form['Name'],
            Data=request.form['Data'],
            Slgon=request.form['Slgon'],
            Hometown=request.form['Hometown'],
            Job=request.form['Job'],
            Video=request.form['Video'],
            Pictures=request.form['Pictures'],
            Thumbnail=request.form['Thumbnail'],
        )
        try:
            db.session.add(Model)
            db.session.commit()
            print( 'add ok')
        except :
            db.session.rollback()
        db.session.close()
        return render_template('form.html',form=form )
    else:
        form = AddForm()
        return render_template('form.html',form=form )

@views.route('/upload', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        for filename in request.files.getlist('photo'):
       
            name = hashlib.md5('admin' + str(time.time())).hexdigest()[:15]
            photos.save(filename, name=name + '.')
        success = True
    else:
        success = False
    return render_template('upload.html', form=form, success=success)

@views.route('/uploaded', methods=['GET','POST'])
def uploaded_file():
    success=1
    if request.method == 'POST':
        print('ok post')
        #  file = request.files['file']
        filelist=[]
        for file in request.files.getlist('file'):
            print(file)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                basepath = os.path.dirname(__file__)
                upload_path = os.path.join(basepath, 'static/upload_file', filename)
                print(filename)
                file.save(upload_path)
                filelist.append(filename) 
        return jsonify({"result":filelist})
    else:
        success='2'
        return render_template('uploadAJAX.html', success=success)

@views.route('/item/<int:user_id>', methods=['GET','POST'])
def item(user_id):
    l='/'
    result=Models.query.filter_by(Id=user_id).first()
    if result:
        return render_template('item.html',link=l, commit=result)
    else:
        return redirect(url_for('err'))
@views.route('/faq/')
def faq():
    l='/'
    return render_template('faq.html', link=l)


