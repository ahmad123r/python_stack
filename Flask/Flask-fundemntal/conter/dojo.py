from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 
@app.route('/',methods=['POST','GET'])
def counter():
    if 'counter' in session:
        session['counter']=session.get('counter')+1
    else:
        session['counter']=1
    c=str(session.get('counter'))
    return render_template('show.html',c=c)
@app.route('/delete-visits/')
def delete_visits():
    session.pop('counter', None) # delete visits
    return 'Visits deleted'
if __name__ == "__main__":
    app.run(debug=True)