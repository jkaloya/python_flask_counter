from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

def viewCounter():
    try:
        session['view'] +=1
    except KeyError:
        session['view'] = 1

@app.route('/')
def index():
    viewCounter()
    return render_template('counter_index.html')

@app.route('/plus2', methods=['get'])
def plus2():
    viewCounter()
    return redirect('/')

@app.route('/reset', methods=['get'])
def reset():
    try:
        session['view'] = 0
    except KeyError:
        session['view'] = 1
    return redirect('/')

app.run(debug=True)
