from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalRangeField
app = Flask(__name__)
V = 20
Pven = 30
Pint = 12
DeltaP = 51
Pavt = 87
SvO2 = 65

@app.route('/admin/sliders', methods=['POST'])
def sliders():
    global V
    global Pven
    global Pint
    global DeltaP
    global Pavt
    global SvO2
    V = request.form['VS']
    Pven = request.form['PvenS']
    Pint = request.form['PintS']
    DeltaP = request.form['DeltaPS']
    Pavt = request.form['PavtS']
    SvO2 = request.form['SvO2S']
    return redirect('/admin')
    
@app.route('/admin')
def hello():
    global V
    global Pven
    global Pint
    global DeltaP
    global Pavt
    global SvO2
    return render_template('base.html', V=V, Pven=Pven, Pint=Pint, DeltaP=DeltaP, Pavt=Pavt, SvO2=SvO2)

@app.route('/admin/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)