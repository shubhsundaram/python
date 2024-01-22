from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello "+name.title()+" Welcome to flask."

if __name__ == '__main__':
    app.run(debug=True)