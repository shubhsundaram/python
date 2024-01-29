from flask import Flask , abort

app = Flask(__name__)

@app.route("/<uname>")
def username(uname):
    # it will throw error if username starts with a digit number.
    if uname[0].isdigit():
        abort(400)
    return "<h1> Hello User, welcome to flask.. </h1>"

if __name__ == "__main__":
    app.run(debug=True)