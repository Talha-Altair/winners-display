from flask import Flask , request, render_template, jsonify
import json

app = Flask(__name__)

def get_json():

    json_file = open("winners.json")
    json_data = json.load(json_file)

    return json_data

def store_data(json_data):

    with open("winners.json", 'w') as outfile:
        json.dump(json_data, outfile)


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
       jr_fpr = request.form.get("jr_fpr")
       intern_name = request.form.get("intern")
       results={
            "fpr": fpr,
            "ffpr": ffpr,
            "learner": learner,
            "writer": writer,
            "mdev": mdev,
            "mentor": mentor,
            "lteam": lteam,
            "tool": tool,
            "jr_fpr": jr_fpr,
            "intern_name" :intern_name 
        }
       print(results)
    store_data(results)

    return render_template('intro.html')

@app.route('/fpr',methods=["GET", "POST"])
def fpr():

    json = get_json()
    
    val = json["fpr"]

    return render_template('ftpr.html',val=val)

@app.route('/jr_fpr',methods=["GET", "POST"])
def jr_fpr():

    json = get_json()
    
    val = json["jr_fpr"]

    return render_template('jr_fpr.html',val=val)

@app.route('/ffpr',methods=["GET", "POST"])
def ffpr():

    json = get_json()
    
    val = json["ffpr"]

    return render_template('ftpr-girl.html',val=val) 

@app.route('/learner',methods=["GET", "POST"])
def learner():

    json = get_json()
    
    val = json["learner"]

    return render_template('learner.html',val=val)        

@app.route('/lteam',methods=["GET", "POST"])
def lteam():

    json = get_json()
    
    val = json["lteam"]
 
    return render_template('learningteam.html',val=val)

@app.route('/tool',methods=["GET", "POST"])
def tool():

    json = get_json()
    
    val = json["tool"]
 
    return render_template('toolresearcher.html',val=val)

@app.route('/writer',methods=["GET", "POST"])
def writer():

    json = get_json()
    
    val = json["writer"]
 
    return render_template('writer.html',val=val)

@app.route('/memdev',methods=["GET", "POST"])
def memdev():

    json = get_json()
    
    val = json["mdev"]
 
    return render_template('memedev.html',val=val)

@app.route('/mentor',methods=["GET", "POST"])
def mentor():

    json = get_json()
    
    val = json["mentor"]
 
    return render_template('mentor.html',val=val)

@app.route('/intern',methods=["GET", "POST"])
def intern_name():

    json = get_json()
    
    val = json["intern_name"]
 
    return render_template('intern.html',val=val)

@app.route('/end')
def end():
 
    return render_template('done.html')  


if __name__ == '__main__':
  app.run(port=8080, debug=True)