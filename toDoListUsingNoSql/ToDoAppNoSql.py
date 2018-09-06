from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config['MONGO_DBNAME']='todorestfullapinosql'
app.config['MONGO_URI']='mongodb://m.asad:55226688shitwrongpasswordshit!@ds147592.mlab.com:47592/todorestfullapinosql'

mongo = PyMongo(app)

## Added Tasks to Database
##@app.route('/add')
#def addTasks():
#    insertQuery=mongo.db.tasks
#    insertQuery.insert({'Title':'FlaskTask', 'Description':'TodoRESTful API - A TDD Approach to Building an API using NoSQL Database', 'Done':0})
#    insertQuery.insert({'Title': 'JavaScriptTask',
#                        'Description': 'Complete JS 40 chapters from "A Smarter Way To Learn JavaScript" ',
#                        'Done': 0})
#    insertQuery.insert({'Title': 'Interview Questions',
#                      'Description': 'Preparation for Job Interviews',
#                      'Done': 0})
#    insertQuery.insert({'Title': 'Tennis',
#                        'Description': 'Play tennis regularly, Health Goals','Done': 1})
#    return 'Added'

@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def getAllTasks():
    tasks=mongo.db.tasks
    output=[]

    for q in tasks.find():
        output.append({'Title':q['Title'], 'Description':q['Description'], 'Done':q['Done']})

    return jsonify({'result': output})





app.run(debug=True)