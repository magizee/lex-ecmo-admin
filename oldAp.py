# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, render_template
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
oxygenFloat = 99.22
pressure1 = 0.25
flowOut = 10.0
flowIn = 10.0

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/<meter>/<value>')
# ‘/<meter>/<value>’ URL is bound with valuePass(meter, value) function.
def valuePass(meter, value):
   global oxygenFloat
   global pressure1
   global flowIn
   global flowOut
   
   if type(meter) != str:
        meter = str(meter)
   elif type(value) != str:
        value = str(value)
   if meter.upper() == 'OXYGEN' or meter.upper() == 'O':
       if value.upper() != 'READ' and value.upper() != 'R':
            oxygenFloat = float(value)
       ##return 'Oxygen value set to: %s' % str(oxygenFloat)
   elif meter.upper() == 'PRESSURE1' or meter.upper() == 'P1':
       if value.upper() != 'READ' and value.upper() != 'R':
           pressure1 = float(value)
   elif meter.upper() == "FLOWOUT" or meter.upper() == 'FO':
       if value.upper() != 'READ' and value.upper() != 'R':
           flowOut = float(value)
   elif meter.upper() == 'FLOWIN' or meter.upper() == 'FI':
       if value.upper() != 'READ' and value.upper() != 'R':
           flowIn = float(value)
       ##return 'Pressure1 value set to: %s' % str(pressure1)    
   ##return 'Non valid meter: %s' % meter
   return redirect('/', 302)   

@app.route('/')

def dash():
    global oxygenFloat
    global pressure1
    returning = 'Oxygen meter: %s' % str(oxygenFloat)
    returning += ' Pressure1: %s' % str(pressure1)
    returning += ' Flow out: %s' % str(flowOut)
    returning += ' Flow in: %s' % str(flowIn)
    return returning

@app.route('/dash')
@app.route('/dashboard')
@app.route('/main')

def toDash():
    return redirect('/', 302)

@app.route('/highPressure')

def highPressure():
    global pressure1
    global flowIn
    global flowOut
    pressure1 = 125.02
    flowOut = 12.3
    flowIn = 13.7
    return redirect('/', 302)

@app.route('/lowOxygen')

def lowOxygen():
    global oxygenFloat
    global pressure1
    oxygenFloat = 85.3
    return redirect('/', 302)

@app.route('/reset')

def reset():
    global oxygenFloat
    global pressure1
    global flowIn
    global flowOut
    oxygenFloat = 99.22
    pressure1 = 0.25
    flowIn = 10.0
    flowOut = 10.0
    return redirect('/', 302)

@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/button-clicked', methods=['POST'])
def buttonClidk():
    print('clicked')
    return redirect('/')
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()