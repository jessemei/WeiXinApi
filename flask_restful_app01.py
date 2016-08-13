#!/usr/bin/env python
#!coding:utf-8
import json
from flask import Flask,jsonify,abort,make_response,request
app = Flask(__name__)
tasks = [
    {
        'id':1,
        'title':u'学习是件快乐的事',
        'description':u'这里会有一些描述信息',
        'done':False
    },
    {
        'id':2,
        'title':u'这是第二件事',
        'description':u'这里会有一些描述信息',
        'done':True
    }
]
@app.route('/jesse/api/tasks',methods=['GET'])
def get_tastks():
    return  jsonify({'tasks':tasks})


@app.route('/jesse/api/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task = filter(lambda t:t['id'] == task_id,tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Fount'}),404)

@app.route('/jesse/api/tasks',methods=['POST'])
def create_tast():
    if not request.json or not "title" in request.json:
        abort(400)
    task = {
        'id':tasks[-1]['id']+1,#获取tasks最后一个id并加1
        'title':request.json['title'],
        'description':request.json.get('description',""),#如果没有给改参数则为空
        'done':False
    }
    tasks.append(task)
    return jsonify({'task':task}),201


@app.route('/jesse/api/update/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    task = filter(lambda t:t['id'] == task_id,tasks) #获取task_id的值通过lambda条件返回等于用户传来id的task
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])  #返回的task是一个列表里面有字典
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@app.route('/jesse/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})
























if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',threaded=True)













