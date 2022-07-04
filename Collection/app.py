from ast import Pass
from flask import Flask, render_template, request
import json
import sqlite3

conn = sqlite3.connect('ni.db')
conn = sqlite3.connect('di.db')
c = conn.cursor()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/idrange', methods=['POST', 'GET'])
def period_scale():
    conn = sqlite3.connect('ni.db')
    c = conn.cursor()
    data1=str(request.form['id1'])
    data2=str(request.form['id2'])
    c.execute("select * from ni where id between '"+data1+"' and '"+data2+"';") 
    period=c.fetchall()
    return render_template('/idrange.html', p=period)
    

@app.route('/iddetails', methods=['POST', 'GET'])
def removename():
    conn = sqlite3.connect('di.db')
    c = conn.cursor()
    num1=str(request.form['number1'])
    num2=str(request.form['number2'])
    c.execute("SELECT * FROM di WHERE id = '"+num1+"' AND code = '"+num2+"' group by pwd;")
    magrange = c.fetchall()
    return render_template('/iddetails.html', m=magrange)


@app.route('/times',methods=['POST','GET'])
def search_magnitude():
    conn = sqlite3.connect('di.db')
    c = conn.cursor()
    data1=str(request.form['code1'])
    data2=str(request.form['code2'])
    data = str(request.form['maxnum'])
    c.execute("select * from di where code between '"+data1+"' AND '"+data2+"' order by id DESC LIMIT '"+data+"';")
    row=c.fetchall()
    return render_template('/times.html',t=row)

if __name__ == '__main__':
    app.debug = True
    app.run()