from flask import Flask, render_template
app = Flask(__name__)    
# @app.route('/')        
# def hello_world():

#     return 'Hello World!'
# @app.route('/dojo') 
# def dojo():
#     return 'Dojo!' 
# @app.route('/say/<name>') 
# def say(name):
#     return f"Hi {name}!" 
# @app.route('/repeat/<int:times>/<name>')
# def repeat(times,name):
#     str=name


#     return (str + '\n')*times
@app.route('/play') 
def two():
    return render_template('pyth.html')     
if __name__=="__main__":    
    app.run(debug=True) 