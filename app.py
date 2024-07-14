# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
oxygenFloat = 25.22

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/<meter>/<value>')
# ‘/’ URL is bound with hello_world() function.
def valuePass(meter, value):
   global oxygenFloat
   if type(meter) != str:
        meter = str(meter)
   if type(value) != str:
        value = str(value)
   if meter == 'oxygen':
       if value != 'read':
            oxygenFloat = float(value)
       return 'Oxygen value set to: %s' % str(oxygenFloat)
   return 'Hello %s!' % value
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
