from flask import Flask,request
from flask.templating import render_template
import threading,os

app = Flask(__name__)

def runFile():
    exec(open(r"./Drowsiness_detection/drowsiness_detection.py").read())

thread = threading.Thread(target=runFile)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/main')
def main():
    return render_template("main.html")

@app.route('/instr')
def instr():
    return render_template("instruction.html")    

@app.route('/start')
def start():
    return render_template("start.html")

@app.route('/load')
def load():
    return render_template("loader.html")  


    
@app.route('/track', methods=['POST'])
def track():
    data = request.form.to_dict()
    if data['status']=='START tracking':
        thread.start()
    if data['status']=='STOP tracking':
        pass     
    return render_template("start.html")  
    
if __name__ == '__main__':
    app.run(debug=True)