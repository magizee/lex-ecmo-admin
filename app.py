from flask import Flask, redirect, render_template, jsonify, request
import random
import json
from flask_wtf import FlaskForm
from wtforms import DecimalRangeField
import time

# Initialize flask app
app = Flask(__name__)

# Define your safety range limits
safety_ranges = {
    'flow_rate': (2.0, 3.0),
    'p_ven': (-10, 10),
    'p_int': (150, 200),
    'p_art': (100, 180),
    't_art': (35, 40),
    'svo2': (70, 90),
    'delta_p': (5, 15),
}

# Example values
flow_rate = 2.52
flow_rateMax = 100
flow_rateMin = 0

p_ven = -11
p_venMax = 100
p_venMin = 0

p_int = 191
p_intMax = 100
p_intMin = 0

p_art = 180
p_artMax = 100
p_artMin = 0

t_art = 37.6
t_artMax = 100
t_artMin = 0

svo2 = 83.0
svo2Max = 100
svo2Min = 0

delta_p = 11
delta_pMax = 100
delta_pMin = 0

rpm = 4000
rpmMax = 8000
rpmMin = 0

# Back end code

def cleanValues():
    global flow_rate
    global flow_rateMax
    global flow_rateMin
    global p_ven
    global p_venMax
    global p_venMin
    global p_int
    global p_intMax
    global p_intMin
    global p_art
    global p_artMax
    global p_artMin
    global t_art
    global t_artMax
    global t_artMin
    global svo2
    global svo2Max
    global svo2Min
    global delta_p
    global delta_pMax
    global delta_pMin
    global rpm
    global rpmMax
    global rpmMin
    flow_rate = round(float(flow_rate),2)
    flow_rateMax = round(float(flow_rateMax),2)
    flow_rateMin = round(float(flow_rateMin),2)
    p_ven = round(float(p_ven),2)
    p_venMax = round(float(p_venMax),2)
    p_venMin = round(float(p_venMin),2)
    p_int = round(float(p_int),2)
    p_intMax = round(float(p_intMax),2)
    p_intMin = round(float(p_intMin),2)
    p_art = round(float(p_art),2)
    p_artMax = round(float(p_artMax),2)
    p_artMin = round(float(p_artMin),2)
    t_art = round(float(t_art),2)
    t_artMax = round(float(t_artMax),2)
    t_artMin = round(float(t_artMin),2)
    svo2 = round(float(svo2),2)
    svo2Max = round(float(svo2Max),2)
    svo2Min = round(float(svo2Min),2)
    delta_p = round(float(delta_p),2)
    delta_pMax = round(float(delta_pMax),2)
    delta_pMin = round(float(delta_pMin),2)
    rpm = int(rpm)
    rpmMax = int(rpmMax)
    rpmMin = int(rpmMin)
@app.route('/admin/setPresets')
def setPresets():
    return render_template('setPresets.html')
@app.route('/admin/setPresets/send', methods=['POST'])
def setPresetsSend():
    global flow_rateMax
    global flow_rateMin
    global p_venMax
    global p_venMin
    global p_intMax
    global p_intMin
    global p_artMax
    global p_artMin
    global t_artMax
    global t_artMin
    global svo2Max
    global svo2Min
    global delta_pMax
    global delta_pMin

    flow_rateMax = request.form['VHigh']
    flow_rateMin = request.form['VLow']
    p_venMax = request.form['PvenHigh']
    p_venMin = request.form['PvenLow']
    p_intMax = request.form['PintHigh']
    p_intMin = request.form['PintLow']
    p_artMax = request.form['PartHigh']
    p_artMin = request.form['PartLow']
    t_artMax = request.form['TartHigh']
    t_artMin = request.form['TartLow']
    svo2Max = request.form['SvO2High']
    svo2Min = request.form['SvO2Low']
    delta_pMax = request.form['DeltaPHigh']
    delta_pMin = request.form['DeltaPLow']
    cleanValues()
    return redirect('/admin')
@app.route('/admin/loading/<scen>', methods=['POST'])
def exampleScenario1Loading(scen):
    timer = request.form['example1Length']
    if timer:
        return render_template('loading.html', scen=scen, timer=timer)
    else:
        return render_template('loading.html', scen=scen, timer=5)

@app.route('/admin/exampleScenario1/<timer>', methods=['GET'])
def exampleScenario1(timer):
    cleanValues()
    if timer.isdigit() == False:
        return redirect('/admin')
    global flow_rate
    global p_ven
    global svo2
    timer = int(timer)
    Vstatic = flow_rate
    PvenStatic = p_ven
    SvO2Static = svo2
    startTime = time.time()
    currentTimer = int(time.time() - startTime)
    print(Vstatic)
    while (currentTimer) <= timer:
        flow_rate = round(Vstatic + (currentTimer/timer) * (65-Vstatic),2)
        p_ven = round(PvenStatic + (currentTimer/timer) * (75-PvenStatic),2)
        svo2 = round(SvO2Static + (currentTimer/timer) * (80-SvO2Static),2)
        currentTimer = int(time.time() - startTime)
    
    return redirect('/admin')
    
@app.route('/admin/sliders', methods=['POST'])
def sliders():
    global flow_rate
    global p_ven
    global p_int
    global delta_p
    global p_art
    global svo2
    global t_art
    print(request.form)
    flow_rate = request.form['VS']
    p_ven = request.form['PvenS']
    p_int = request.form['PintS']
    p_art = request.form['PartS']
    delta_p = request.form['DeltaPS']
    t_art = request.form['TartS']
    svo2 = request.form['SvO2S']
    cleanValues()
    return redirect('/admin')
    
@app.route('/admin')
def controlPanel():
    global flow_rate
    global flow_rateMax
    global flow_rateMin
    global p_ven
    global p_venMax
    global p_venMin
    global p_int
    global p_intMax
    global p_intMin
    global p_art
    global p_artMax
    global p_artMin
    global t_art
    global t_artMax
    global t_artMin
    global svo2
    global svo2Max
    global svo2Min
    global delta_p
    global delta_pMax
    global delta_pMin
    global rpm
    cleanValues()
    return render_template('admin.html', V=flow_rate, Pven=p_ven, Pint=p_int, Part=p_art, DeltaP=delta_p, Tart=t_art, SvO2=svo2, VMin=flow_rateMin, VMax=flow_rateMax, PvenMin=p_venMin, PvenMax=p_venMax, PintMin=p_intMin, PintMax=p_intMax, PartMax=p_artMax, PartMin=p_artMin, TartMin=t_artMin, TartMax=t_artMax, SvO2Min=svo2Min, SvO2Max=svo2Max, DeltaPMin=delta_pMin, DeltaPMax=delta_pMax)

@app.route('/admin/about')
def about():
    return render_template('about.html')

# Front end code
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)


def check_safety(value, range):
    return range[0] <= value <= range[1]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    safety_status = {
        'flow_rate': check_safety(flow_rate, safety_ranges['flow_rate']),
        'p_ven': check_safety(p_ven, safety_ranges['p_ven']),
        'p_int': check_safety(p_int, safety_ranges['p_int']),
        'p_art': check_safety(p_art, safety_ranges['p_art']),
        't_art': check_safety(t_art, safety_ranges['t_art']),
        'svo2': check_safety(svo2, safety_ranges['svo2']),
        'delta_p': check_safety(delta_p, safety_ranges['delta_p']),
    }
    return render_template('dashboard.html', rpm=rpm, flow_rate=flow_rate, p_ven=p_ven, p_int=p_int, p_art=p_art, t_art=t_art, svo2=svo2, delta_p=delta_p, safety_status=safety_status)

@app.route('/update')
def update():
    # Update example values (in a real application, these would be fetched from sensors or a database)
    """
    global flow_rate, p_ven, p_int, p_art, t_art, svo2, delta_p, rpm
    flow_rate = round(random.uniform(2.0, 3.0), 2)
    p_ven = random.randint(-15, 15)
    p_int = random.randint(140, 210)
    p_art = random.randint(90, 190)
    t_art = round(random.uniform(34.0, 41.0), 1)
    svo2 = round(random.uniform(65.0, 95.0), 1)
    delta_p = random.randint(0, 20)
    rpm = random.randint(3500, 4500)
    """
    safety_status = {
        'flow_rate': check_safety(flow_rate, safety_ranges['flow_rate']),
        'p_ven': check_safety(p_ven, safety_ranges['p_ven']),
        'p_int': check_safety(p_int, safety_ranges['p_int']),
        'p_art': check_safety(p_art, safety_ranges['p_art']),
        't_art': check_safety(t_art, safety_ranges['t_art']),
        'svo2': check_safety(svo2, safety_ranges['svo2']),
        'delta_p': check_safety(delta_p, safety_ranges['delta_p'])
    }
    return jsonify(
        flow_rate=flow_rate, 
        p_ven=p_ven, 
        p_int=p_int, 
        p_art=p_art, 
        t_art=t_art, 
        svo2=svo2, 
        delta_p=delta_p, 
        rpm=rpm, 
        safety_status=safety_status
    )

@app.route('/rpm')
def getRPM():
    global rpm
    return jsonify(
        rpm=rpm
        )

if __name__ == '__main__':
    app.run(debug=True)
