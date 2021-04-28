from flask import Blueprint
from app.functions import *

router = Blueprint('router',__name__)

@router.route('/test')
def home():
    return "<h1>Test</h1>"

@router.route('/create/<string:type>/<int:uid>',methods=['POST']) 
def operation1(type,uid):
    return (create(type,uid))

@router.route('/read/<string:type>/<int:uid>',methods=['GET'])
def operation2(type,uid):
    return (read(type,uid))

@router.route('/update/<string:type>/<int:uid>',methods=['POST'])
def operation3(type,uid):
    return (update(type,uid))

@router.route('/delete/<string:type>/<int:uid>',methods=['POST'])
def operation4(type,uid):
    return (delete(type,uid))
