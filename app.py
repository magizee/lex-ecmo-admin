from flask import Flask, redirect, render_template

app = Flask(__name__)
oxygen = 1.05

@app.route('/')
def hello():
    return render_template('index.html',oxygen=oxygen)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()