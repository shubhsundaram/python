from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def squarenumber():
    if request.method == 'POST':
        if (request.form['num']==''):
            return "<html><body> <h1> Enter a Valid Number </h1></body></html>"
        else:
          # If user has entered a number,
          # fetch the number from args attribute of the request accessing its 'id' from HTML
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html', squareofnum=sq, num=number)
    if request.method == 'GET':
        return render_template('squarenum.html')
        
if __name__ == "__main__":
    app.run(debug=True)