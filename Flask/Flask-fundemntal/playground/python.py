from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')        
def hello_world():

    return 'Hello World!'
@app.route('/dojo') 
def dojo():
    return 'Dojo!' 
@app.route('/say/<name>') 
def say(name):
    return f"Hi {name}!" 
@app.route('/repeat/<int:times>/<name>')
def repeat(times,name):
    str=name

@app.route('/play/<cont>/<color>') 
def olay(cont,color):
    return render_template('index.html',cont=int(cont),color=color)


    return (str + '\n')*times    
if __name__=="__main__":    
    app.run(debug=True)