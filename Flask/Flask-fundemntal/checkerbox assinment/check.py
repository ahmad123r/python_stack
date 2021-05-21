from flask import Flask, render_template
app = Flask(__name__)
@app.route('/<int:x>/<int:y>')
def index(x,y):
    return render_template("ht.html",x=x,y=y)	
if __name__=="__main__":
    app.run(debug=True)