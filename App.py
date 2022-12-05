import flask
from flask import Flask, render_template, request

app = Flask(__name__)

def init():
    print("initializing... ") 
  
@app.route('/')
def index():
    return render_template('index.html')
 

if __name__ == '__main__':
    init()
    app.run(debug=True, port=9090)
   