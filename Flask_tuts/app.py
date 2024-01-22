from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def home():
    # we will automatically be redirected to the helloworld page
    # as we hot the base landing page.
    return redirect('/helloworld')

@app.route('/helloworld')
def hello_world():
    return "<p> Hello , world from \
        redirected page..!</p>"
        
if __name__ == '__main__':
    app.run(debug=True)