from flask import Flask , request, render_template, jsonify
import json
from flask_pymongo import PyMongo
import os
from decouple import config
from bson.json_util import dumps
import logging
from pprint import pprint

app = Flask(__name__)

# cluster = MongoClient('mongodb+srv://Altair:Altair@cluster0.xvmvm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

# db = cluster["SpinTime"]
# col = db["winners"]

# app.config['MONGO_URI'] = config('MONGO_URI') #Create .env first
# mongo                   = PyMongo(app)
# col                     = mongo.db.col


@app.route('/') #Defining Root Node
def winners():
    return render_template('intro.html')  

@app.route('/details',methods=["GET", "POST"])
def details():
    if request.method == "POST":
       fpr = request.form.get("fpr")
       ffpr = request.form.get("ffpr")
       learner = request.form.get("learner")
       lteam = request.form.get("lteam")
       mdev = request.form.get("mdev")
       mentor = request.form.get("mentor")
       tool = request.form.get("tool") 
       writer = request.form.get("writer")
       jr_fpr = request.form.get("jr_fpr")
       results={1:fpr, 2: ffpr,3:learner,4:lteam,5:mdev,6:mentor,7:tool,8:writer,9:jr_fpr}
       print(results)
    # col.insert_many([
    #  { "Title":"fpr","winner": fpr},
    #  { "Title":"ffpr", "winner": ffpr},
    #  { "Title":"learner","winner": learner},
    #  { "Title":"lteam", "winner": lteam},
    #  { "Title":"mdev","winner": mdev},
    #  { "Title":"mentor", "winner": mentor},
    #  { "Title":"tool","winner": tool},
    #  { "Title":"writer", "winner": writer},
    #  { "Title":"jr_fpr", "winner": jr_fpr}
    # ])
    return render_template('intro.html')

@app.route('/fpr',methods=["GET", "POST"])
def fpr():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="fpr":
    #         val=x['winner']

    return render_template('ftpr.html')

@app.route('/jr_fpr',methods=["GET", "POST"])
def jr_fpr():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="jr_fpr":
    #         val=x['winner']

    return render_template('jr_fpr.html')

@app.route('/ffpr',methods=["GET", "POST"])
def ffpr():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="ffpr":
    #         val=x['winner']

    return render_template('ftpr-girl.html') 

@app.route('/learner',methods=["GET", "POST"])
def learner():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="learner":
    #         val=x['winner']

    return render_template('learner.html')        

@app.route('/lteam',methods=["GET", "POST"])
def lteam():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="lteam":
    #         val=x['winner']

    return render_template('learningteam.html')

@app.route('/tool',methods=["GET", "POST"])
def tool():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="tool":
    #         val=x['winner']

    return render_template('toolresearcher.html')

@app.route('/writer',methods=["GET", "POST"])
def writer():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="writer":
    #         val=x['winner']

    return render_template('writer.html')

@app.route('/memdev',methods=["GET", "POST"])
def memdev():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="mdev":
    #         val=x['winner']

    return render_template('memedev.html')

@app.route('/mentor',methods=["GET", "POST"])
def mentor():
    # for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
    #     if x['Title']=="mentor":
    #         val=x['winner']

    return render_template('mentor.html')

@app.route('/end')
def end():
    return render_template('done.html')  


if __name__ == '__main__':
  app.run(port=8080, debug=True)