from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import DecimalRangeField
import time
app = Flask(__name__)
V = 20
Pven = 30
Pint = 12
DeltaP = 51
Pavt = 87
SvO2 = 65
sliderURL = "/admin/sliders"

def cleanValues():
    global V
    global Pven
    global Pint
    global DeltaP
    global Pavt
    global SvO2
    V = float(V)
    Pven = float(Pven)
    Pint = float(Pint)
    DeltaP = float(DeltaP)
    Pavt = float(Pavt)
    SvO2 = float(SvO2)
@app.route('/admin/exampleScenario1Loading', methods=['POST'])
def exampleScenario1Loading():
    timer = request.form['example1Length']
    if timer:
        return render_template('loading.html', timer=timer)
    else:
        return render_template('loading.html', timer=5)

@app.route('/admin/exampleScenario1/<timer>', methods=['GET'])
def exampleScenario1(timer):
    cleanValues()
    if timer.isdigit() == False:
        return redirect('/admin')
    global V
    global Pven
    global SvO2
    timer = int(timer)
    Vstatic = V
    PvenStatic = Pven
    SvO2Static = SvO2
    startTime = time.time()
    currentTimer = int(time.time() - startTime)
    print(Vstatic)
    while (currentTimer) <= timer:
        V = Vstatic + (currentTimer/timer) * (65-Vstatic)
        Pven = PvenStatic + (currentTimer/timer) * (75-PvenStatic)
        SvO2 = SvO2Static + (currentTimer/timer) * (80-SvO2Static)
        currentTimer = int(time.time() - startTime)
    
    return redirect('/admin')
    
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
    cleanValues()
    return redirect('/admin')
    
@app.route('/admin')
def hello():
    global V
    global Pven
    global Pint
    global DeltaP
    global Pavt
    global SvO2
    cleanValues()
    return render_template('base.html', V=V, Pven=Pven, Pint=Pint, DeltaP=DeltaP, Pavt=Pavt, SvO2=SvO2, sliderURL=sliderURL)

@app.route('/admin/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)