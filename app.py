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
       tool = request.form.get("tool") 
       writer = request.form.get("writer")
       intern_name = request.form.get("intern")
       results={
            "fpr": fpr,
            "ffpr": ffpr,
            "writer": writer,
            "tool": tool,
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

@app.route('/ffpr',methods=["GET", "POST"])
def ffpr():

    json = get_json()
    
    val = json["ffpr"]

    return render_template('ftpr-girl.html',val=val) 


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