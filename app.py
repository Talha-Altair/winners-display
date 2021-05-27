from flask import Flask,render_template,request
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cluster = MongoClient('mongodb+srv://talha:talha@cluster0.xvmvm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')

db = cluster["SpinTime"]
col = db["winners"]

@app.route('/') #Defining Root Node
def winners():
    return render_template('winners.html')  

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
       results={1:fpr, 2: ffpr,3:learner,4:lteam,5:mdev,6:mentor,7:tool,8:writer}
    col.insert_many([
     { "Title":"fpr","winner": fpr},
     { "Title":"ffpr", "winner": ffpr},
     { "Title":"learner","winner": learner},
     { "Title":"lteam", "winner": lteam},
     { "Title":"mdev","winner": mdev},
     { "Title":"mentor", "winner": mentor},
     { "Title":"tool","winner": tool},
     { "Title":"writer", "winner": writer}
   ])
    return render_template('intro.html')

@app.route('/fpr',methods=["GET", "POST"])
def fpr():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="fpr":
            val=x['winner']

    return render_template('ftpr.html',val=val)

@app.route('/ffpr',methods=["GET", "POST"])
def ffpr():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="ffpr":
            val=x['winner']

    return render_template('ftpr-girl.html',val=val) 

@app.route('/learner',methods=["GET", "POST"])
def learner():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="learner":
            val=x['winner']

    return render_template('learner.html',val=val)        

@app.route('/lteam',methods=["GET", "POST"])
def lteam():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="lteam":
            val=x['winner']

    return render_template('learningteam.html',val=val)

@app.route('/tool',methods=["GET", "POST"])
def tool():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="tool":
            val=x['winner']

    return render_template('toolresearcher.html',val=val)

@app.route('/writer',methods=["GET", "POST"])
def writer():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="writer":
            val=x['winner']

    return render_template('writer.html',val=val)

@app.route('/memdev',methods=["GET", "POST"])
def memdev():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="mdev":
            val=x['winner']

    return render_template('memedev.html',val=val)

@app.route('/mentor',methods=["GET", "POST"])
def mentor():
    for x in col.find({},{ "_id": 0, "Title": 1, "winner": 1 }):
        if x['Title']=="mentor":
            val=x['winner']

    return render_template('mentor.html',val=val)

@app.route('/end')
def end():
    return render_template('done.html')  


if __name__ == '__main__':
  app.run(port=8080, debug=True)