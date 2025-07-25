

from flask import Flask,render_template


app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
 
@app.route('/about',methods=['GET'])
def about():
    return render_template("about.html")

@app.route('/services',methods=['GET'])
def services():
    return render_template("services.html")

@app.route('/contact',methods=['GET'])
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)


