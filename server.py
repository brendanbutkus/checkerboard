from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkerboard1():
    return render_template("index.html", row=8, box=8, color_one='blue', color_two='black' )
@app.route('/<int:num>')
def checkerboard2(num):
    return render_template("index.html", row=num, box=8, color_one='blue', color_two='black')
@app.route('/<int:num1>/<int:num2>')
def checkerboard3(num1,num2):
    return render_template("index.html" , row=num1, box=num2, color_one='blue', color_two='black')
@app.route('/<int:num1>/<int:num2>/<string:col1>/<string:col2>')
def checkerboard4(num1,num2,col1,col2):
    return render_template("index.html" , row=num1, box=num2, color_one=col1, color_two=col2)
    

if __name__=="__main__":
    app.run(debug=True)

