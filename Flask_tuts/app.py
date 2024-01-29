from flask import Flask, redirect, url_for , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/success')
def success():
    return "login sucessfully...!"
        
@app.route('/login',methods=['GET','POST'])
def login():
    
    #if method is poat and uername is admin then redirect to success.
    if request.method == 'POST' and request.form["username"] == "admin":
        return redirect(url_for("success"))
    # if the method is get and username is not admin
    # then redirect to index..
    return redirect(url_for('index'))
   
if __name__ == '__main__':
    app.run(debug=True)