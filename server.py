from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hi/<name>')
def hi(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:number>/<string:word>')
def repeat():
    return "word" * number

if __name__ == "__main__":
    app.run(debug = True)